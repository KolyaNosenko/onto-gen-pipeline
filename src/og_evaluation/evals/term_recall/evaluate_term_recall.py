
from __future__ import annotations

import csv
import json
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from ragas import Dataset, Experiment

from og_evaluation.evals.failure_writer import write_failure_log
from og_evaluation.evals.term_recall.experiments import term_recall_experiment
from og_evaluation.evals.term_recall.metrics import (
    calculate_term_recall_summary,
)
from og_evaluation.pipeline_cache import TtlDiskCache
from og_evaluation.workflows.ontology_generation_workflow_factory import (
    CompiledOntologyWorkflow,
)

logger = logging.getLogger(__name__)


async def evaluate_term_recall(
    dataset: Dataset,
    workflow: CompiledOntologyWorkflow,
    cache: TtlDiskCache,
    experiment_name: str,
    output_dir: Path,
    model_id: str,
    retry: int = 0,
) -> dict:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    experiment_results: Experiment = await term_recall_experiment.arun(
        dataset=dataset,
        name=experiment_name,
        workflow=workflow,
        cache=cache,
        retry=retry,
    )

    rows = list(experiment_results)
    summary = calculate_term_recall_summary(rows)

    _write_per_row_csv(rows, output_dir / "per_row.csv")
    _write_summary_json(summary, output_dir / "summary.json")
    _write_manifest(
        output_dir / "manifest.json",
        experiment_name=experiment_name,
        model_id=model_id,
        n_rows=len(rows),
    )
    _persist_predictions(rows, dataset, cache, output_dir / "predictions")

    print(
        f"term_recall macro={summary['macro_recall']:.3f} "
        f"median={summary['median_recall']:.3f} "
        f"perfect={summary['perfect_count']}/{summary['n']}"
    )
    return summary


def _write_per_row_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = [
        "id",
        "title",
        "n_gold_entities",
        "score",
        "pipeline_status",
        "outcome",
        "predicted_ttl_size",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field) for field in fields})


def _write_summary_json(summary: dict, path: Path) -> None:
    path.write_text(json.dumps(summary, indent=2), encoding="utf-8")


def _write_manifest(
    path: Path,
    *,
    experiment_name: str,
    model_id: str,
    n_rows: int,
) -> None:
    manifest = {
        "experiment_name": experiment_name,
        "metric": "term_recall",
        "model_id": model_id,
        "n_rows": n_rows,
        "git_sha": _git_sha(),
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
    }
    path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def _git_sha() -> str | None:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except Exception:  # pylint: disable=broad-except
        return None


def _persist_predictions(
    rows: list[dict], dataset: Dataset, cache: TtlDiskCache, predictions_dir: Path
) -> None:
    predictions_dir.mkdir(parents=True, exist_ok=True)
    text_by_id: dict[int, str] = {}
    for record in dataset:
        try:
            text_by_id[int(record["id"])] = record["text"]
        except (KeyError, TypeError, ValueError):
            continue
    for row in rows:
        row_id = row.get("id")
        if row_id is None:
            continue
        text = text_by_id.get(int(row_id))
        if text is None:
            continue
        artifacts = cache.get(text)
        if artifacts is not None:
            (predictions_dir / f"{row_id}.ttl").write_text(
                artifacts.ttl, encoding="utf-8"
            )
            if artifacts.main_py is not None:
                (predictions_dir / f"{row_id}.main.py").write_text(
                    artifacts.main_py, encoding="utf-8"
                )
        if row.get("pipeline_status") and row.get("pipeline_status") != "ok":
            write_failure_log(
                predictions_dir,
                row_id=row_id,
                pipeline_status=row.get("pipeline_status", "unknown"),
                text_snapshot=text,
                failure_traceback=row.get("failure_traceback"),
            )
