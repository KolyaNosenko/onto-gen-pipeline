
from __future__ import annotations

from typing import Iterable

from ragas import Experiment
from ragas.metrics import numeric_metric
from ragas.metrics.result import MetricResult

from og_evaluation.evals.structural.ontology_counts import (
    StructuralCounts,
    count_structural,
)


_INT_FIELDS: tuple[str, ...] = (
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
    "n_cycle_classes",
)

_BOOL_FIELDS: tuple[str, ...] = ("has_taxonomy_cycle",)

_RATIO_FIELDS: tuple[str, ...] = (
    "relationship_richness",
    "inheritance_richness",
    "attribute_richness",
    "class_richness",
    "average_population",
    "tangledness",
    "mean_taxonomy_depth",
)

_OPTIONAL_INT_FIELDS: tuple[str, ...] = (
    "max_taxonomy_depth",
    "max_taxonomy_breadth",
)


@numeric_metric(name="structural", allowed_values=(0.0, 1.0))
def structural_metric(prediction_ttl: str) -> MetricResult:
    counts = count_structural(prediction_ttl)
    if counts is None:
        return MetricResult(value=0.0, reason="empty or unparseable ttl")
    reason = (
        f"classes={counts.n_classes} "
        f"properties={counts.n_properties} "
        f"(object={counts.n_object_properties}, "
        f"data={counts.n_data_properties}, "
        f"annotation={counts.n_annotation_properties}) "
        f"individuals={counts.n_individuals} "
        f"axioms={counts.n_axioms} "
        f"RR={_fmt(counts.relationship_richness)} "
        f"IR={_fmt(counts.inheritance_richness)} "
        f"AR={_fmt(counts.attribute_richness)} "
        f"CR={_fmt(counts.class_richness)} "
        f"AP={_fmt(counts.average_population)}"
    )
    return MetricResult(value=1.0, reason=reason)


def _fmt(value: float | None) -> str:
    return f"{value:.3f}" if value is not None else "n/a"


def calculate_structural_summary(
    experiment_results: Experiment | Iterable[dict],
) -> dict:
    rows = list(experiment_results)
    n = len(rows)
    if n == 0:
        empty: dict = {"n": 0}
        for field in _INT_FIELDS:
            empty[f"mean_{field}"] = 0.0
        for field in _OPTIONAL_INT_FIELDS:
            empty[f"mean_{field}"] = None
            empty[f"n_{field}_defined"] = 0
        for field in _RATIO_FIELDS:
            empty[f"mean_{field}"] = None
            empty[f"n_{field}_defined"] = 0
        for field in _BOOL_FIELDS:
            empty[f"rate_{field}"] = 0.0
        empty["empty_ttl_count"] = 0
        return empty

    summary: dict = {"n": n}
    for field in _INT_FIELDS:
        values = [int(row.get(field, 0) or 0) for row in rows]
        summary[f"mean_{field}"] = sum(values) / n

    for field in _OPTIONAL_INT_FIELDS + _RATIO_FIELDS:
        defined = [
            row.get(field) for row in rows if row.get(field) is not None
        ]
        summary[f"n_{field}_defined"] = len(defined)
        summary[f"mean_{field}"] = (
            sum(defined) / len(defined) if defined else None
        )

    for field in _BOOL_FIELDS:
        positives = sum(1 for row in rows if bool(row.get(field)))
        summary[f"rate_{field}"] = positives / n

    summary["empty_ttl_count"] = sum(
        1 for row in rows if not int(row.get("n_axioms", 0) or 0)
    )
    return summary


__all__ = [
    "StructuralCounts",
    "calculate_structural_summary",
    "structural_metric",
]
