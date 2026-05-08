
from __future__ import annotations

from typing import Iterable

from ragas import Experiment
from ragas.metrics import numeric_metric
from ragas.metrics.result import MetricResult

from og_evaluation.evals.link_recall.edge_extractor import (
    extract_edges,
    normalize_form,
)


def _pair_matches(
    head_mentions: list[str],
    tail_mentions: list[str],
    edges: set[frozenset[str]],
) -> bool:
    head_norm = {normalize_form(m) for m in head_mentions if m}
    tail_norm = {normalize_form(m) for m in tail_mentions if m}
    for head in head_norm:
        for tail in tail_norm:
            if not head or not tail or head == tail:
                continue
            if frozenset({head, tail}) in edges:
                return True
    return False


@numeric_metric(name="link_recall", allowed_values=(0.0, 1.0))
def link_recall_metric(
    prediction_ttl: str,
    head_mentions: list[list[str]],
    tail_mentions: list[list[str]],
) -> MetricResult:
    if not head_mentions:
        return MetricResult(value=0.0, reason="no gold relations")
    if len(head_mentions) != len(tail_mentions):
        return MetricResult(
            value=0.0,
            reason="head/tail mentions length mismatch",
        )

    edges = extract_edges(prediction_ttl)
    if not edges:
        return MetricResult(
            value=0.0,
            reason="empty or unparseable ttl",
        )

    matched = 0
    for head, tail in zip(head_mentions, tail_mentions):
        if _pair_matches(head, tail, edges):
            matched += 1
    total = len(head_mentions)
    recall = matched / total
    return MetricResult(
        value=recall,
        reason=f"matched {matched}/{total} gold pairs",
    )


def calculate_link_recall_summary(
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
