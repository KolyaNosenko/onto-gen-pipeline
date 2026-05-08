
from __future__ import annotations

from typing import Iterable

from ragas import Experiment
from ragas.metrics import numeric_metric
from ragas.metrics.result import MetricResult

from og_evaluation.evals.term_recall.ontology_signature import (
    extract_searchable_text,
)
from og_evaluation.quality.oracle_recall import (
    compute_oracle_recall_with_variants,
)


@numeric_metric(name="term_recall", allowed_values=(0.0, 1.0))
def term_recall_metric(
    prediction_ttl: str,
    entities: list[str],
    entity_mentions: list[list[str]],
) -> MetricResult:
    searchable = extract_searchable_text(prediction_ttl)
    if not searchable:
        return MetricResult(value=0.0, reason="empty or unparseable ttl")
    if not entities:
        return MetricResult(value=0.0, reason="no gold entities")
    result = compute_oracle_recall_with_variants(
        text=searchable,
        gold_match_sets=entity_mentions,
        canonical_labels=entities,
    )
    matched_str = ", ".join(result.matched_labels) or "none"
    return MetricResult(
        value=result.recall,
        reason=f"matched {result.matched}/{result.total}: {matched_str}",
    )


def calculate_term_recall_summary(
    experiment_results: Experiment | Iterable[dict],
) -> dict:
    rows = list(experiment_results)
    n = len(rows)
    if n == 0:
        return {"n": 0, "macro_recall": 0.0, "median_recall": 0.0, "perfect_count": 0}
    scores = sorted(float(r.get("score", 0.0)) for r in rows)
    macro = sum(scores) / n
    median = scores[n // 2] if n % 2 == 1 else (scores[n // 2 - 1] + scores[n // 2]) / 2
    perfect = sum(1 for s in scores if s >= 1.0)
    return {
        "n": n,
        "macro_recall": macro,
        "median_recall": median,
        "perfect_count": perfect,
    }
