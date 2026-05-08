
from __future__ import annotations

import csv
import json
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from ragas import Dataset, Experiment

from og_evaluation.evals.failure_writer import write_failure_log
from og_evaluation.evals.oops.experiments import oops_experiment
from og_evaluation.evals.oops.metrics import calculate_oops_summary
from og_evaluation.pipeline_cache import TtlDiskCache
from og_evaluation.workflows.ontology_generation_workflow_factory import (
    CompiledOntologyWorkflow,
)

logger = logging.getLogger(__name__)


async def evaluate_oops(
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

    experiment_results: Experiment = await oops_experiment.arun(
        dataset=dataset,
        name=experiment_name,
        workflow=workflow,
        cache=cache,
        retry=retry,
    )

    rows = list(experiment_results)
    summary = calculate_oops_summary(rows)

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
        f"oops on n={summary['n']}: "
        f"clean_rate={summary['clean_rate']:.3f} "
        f"critical_clean_rate={summary['critical_clean_rate']:.3f} "
        f"important_clean_rate={summary['important_clean_rate']:.3f}; "
        f"mean_pitfalls={summary['mean_pitfalls']:.1f} "
        f"(crit={summary['mean_critical']:.2f}, "
        f"imp={summary['mean_important']:.2f}, "
        f"min={summary['mean_minor']:.2f}); "
        f"mean_weighted={summary['mean_pitfall_score_weighted']:.2f}; "
        f"top_codes={list(summary['pitfalls_by_code'].items())[:5]}"
    )
    return summary


def _write_per_row_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = [
        "id",
        "title",
        "score",
        "oops_outcome",
        "criticality_tier",
        "total_pitfalls",
        "n_critical",
        "n_important",
        "n_minor",
        "pitfall_score_weighted",
        "pitfalls_by_importance",
        "pitfalls_by_code",
        "total_affected_elements",
        "pipeline_status",
        "predicted_ttl_size",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "id": row.get("id"),
                    "title": row.get("title"),
                    "score": row.get("score"),
                    "oops_outcome": row.get("oops_outcome"),
                    "criticality_tier": row.get("criticality_tier"),
                    "total_pitfalls": row.get("total_pitfalls"),
                    "n_critical": row.get("n_critical"),
                    "n_important": row.get("n_important"),
                    "n_minor": row.get("n_minor"),
                    "pitfall_score_weighted": row.get("pitfall_score_weighted"),
                    "pitfalls_by_importance": json.dumps(
                        row.get("pitfalls_by_importance") or {},
                        ensure_ascii=False,
                    ),
                    "pitfalls_by_code": json.dumps(
                        row.get("pitfalls_by_code") or {},
                        ensure_ascii=False,
                    ),
                    "total_affected_elements": row.get("total_affected_elements"),
                    "pipeline_status": row.get("pipeline_status"),
                    "predicted_ttl_size": row.get("predicted_ttl_size"),
                }
            )


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
        "metric": "oops_pitfalls",
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
        # Detailed pitfall list per row, for human audit.
        pitfalls = row.get("pitfalls") or []
        if pitfalls:
            (predictions_dir / f"{row_id}.pitfalls.json").write_text(
                json.dumps(pitfalls, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
