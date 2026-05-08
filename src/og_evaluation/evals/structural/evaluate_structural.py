
from __future__ import annotations

import csv
import json
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from ragas import Dataset, Experiment

from og_evaluation.evals.failure_writer import write_failure_log
from og_evaluation.evals.structural.experiments import structural_experiment
from og_evaluation.evals.structural.metrics import (
    calculate_structural_summary,
)
from og_evaluation.pipeline_cache import TtlDiskCache
from og_evaluation.workflows.ontology_generation_workflow_factory import (
    CompiledOntologyWorkflow,
)

logger = logging.getLogger(__name__)


async def evaluate_structural(
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

    experiment_results: Experiment = await structural_experiment.arun(
        dataset=dataset,
        name=experiment_name,
        workflow=workflow,
        cache=cache,
        retry=retry,
    )

    rows = list(experiment_results)
    summary = calculate_structural_summary(rows)

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
        f"structural on n={summary['n']}: "
        f"mean_classes={summary['mean_n_classes']:.1f} "
        f"mean_properties={summary['mean_n_properties']:.1f} "
        f"(object={summary['mean_n_object_properties']:.1f}, "
        f"data={summary['mean_n_data_properties']:.1f}, "
        f"annotation={summary['mean_n_annotation_properties']:.1f}); "
        f"mean_individuals={summary['mean_n_individuals']:.1f}; "
        f"mean_axioms={summary['mean_n_axioms']:.1f}; "
        f"RR={_fmt_ratio(summary.get('mean_relationship_richness'))} "
        f"IR={_fmt_ratio(summary.get('mean_inheritance_richness'))} "
        f"AR={_fmt_ratio(summary.get('mean_attribute_richness'))} "
        f"CR={_fmt_ratio(summary.get('mean_class_richness'))} "
        f"AP={_fmt_ratio(summary.get('mean_average_population'))}; "
        f"taxonomy: roots={summary['mean_n_root_classes']:.1f} "
        f"leaves={summary['mean_n_leaf_classes']:.1f} "
        f"orphans={summary['mean_n_orphan_classes']:.1f} "
        f"components={summary['mean_n_taxonomy_components']:.1f} "
        f"cycle_rate={summary.get('rate_has_taxonomy_cycle', 0.0):.3f}"
    )
    return summary


def _fmt_ratio(value: float | None) -> str:
    return f"{value:.3f}" if value is not None else "n/a"


def _write_per_row_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = [
        "id",
        "title",
        "score",
        "n_classes",
        "n_object_properties",
        "n_data_properties",
        "n_annotation_properties",
        "n_properties",
        "n_non_is_a_properties",
        "n_individuals",
        "n_subclass_axioms",
        "n_axioms",
        "n_classes_with_instances",
        "n_classes_with_multiple_parents",
        "n_data_property_domain_triples",
        "n_root_classes",
        "n_leaf_classes",
        "n_orphan_classes",
        "n_taxonomy_components",
        "has_taxonomy_cycle",
        "n_cycle_classes",
        "max_taxonomy_depth",
        "max_taxonomy_breadth",
        "relationship_richness",
        "inheritance_richness",
        "attribute_richness",
        "class_richness",
        "average_population",
        "mean_taxonomy_depth",
        "tangledness",
        "pipeline_status",
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
        "metric": "structural",
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
