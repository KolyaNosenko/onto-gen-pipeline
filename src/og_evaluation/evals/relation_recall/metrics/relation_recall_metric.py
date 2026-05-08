
from __future__ import annotations

import re
from typing import Iterable

from ragas import Experiment
from ragas.metrics import numeric_metric
from ragas.metrics.result import MetricResult

from og_evaluation.evals.link_recall.edge_extractor import normalize_form
from og_evaluation.evals.relation_recall.edge_extractor import (
    extract_typed_edges,
)


def _label_pattern(label: str) -> re.Pattern[str]:
    tokens = label.strip().split()
    if not tokens:
        return re.compile(r"$^")
    pattern = r"\b" + r"\s+".join(re.escape(t) for t in tokens) + r"\b"
    return re.compile(pattern, flags=re.IGNORECASE)


def _triple_matches(
    head: list[str],
    tail: list[str],
    predicate: list[str],
    edges: set[tuple[frozenset[str], str]],
) -> bool:
    head_norm = {normalize_form(m) for m in head if m}
    tail_norm = {normalize_form(m) for m in tail if m}
    rel_patterns = [
        _label_pattern(rel) for rel in predicate if rel and rel.strip()
    ]
    if not head_norm or not tail_norm or not rel_patterns:
        return False
    for pair, predicate in edges:
        if not pair.issubset(head_norm | tail_norm):
            continue
        if not (pair & head_norm) or not (pair & tail_norm):
            continue
        if any(pattern.search(predicate) for pattern in rel_patterns):
            return True
    return False


@numeric_metric(name="relation_recall", allowed_values=(0.0, 1.0))
def relation_recall_metric(
    prediction_ttl: str,
    head_mentions: list[list[str]],
    tail_mentions: list[list[str]],
    relation_aliases: list[list[str]],
) -> MetricResult:
    if not head_mentions:
        return MetricResult(value=0.0, reason="no gold triples")
    if not (
        len(head_mentions)
        == len(tail_mentions)
        == len(relation_aliases)
    ):
        return MetricResult(
            value=0.0,
            reason="head/tail/predicate length mismatch",
        )

    edges = extract_typed_edges(prediction_ttl)
    if not edges:
        return MetricResult(value=0.0, reason="empty or unparseable ttl")

    matched = 0
    for head, tail, predicate in zip(
        head_mentions, tail_mentions, relation_aliases
    ):
        if _triple_matches(head, tail, predicate, edges):
            matched += 1
    total = len(head_mentions)
    recall = matched / total
    return MetricResult(
        value=recall,
        reason=f"matched {matched}/{total} gold triples",
    )


def calculate_relation_recall_summary(
    experiment_results: Experiment | Iterable[dict],
) -> dict:
    rows = list(experiment_results)
    n = len(rows)
    if n == 0:
        return {
            "n": 0,
            "macro_recall": 0.0,
            "median_recall": 0.0,
            "perfect_count": 0,
        }
    scores = sorted(float(r.get("score", 0.0)) for r in rows)
    macro = sum(scores) / n
    median = (
        scores[n // 2]
        if n % 2 == 1
        else (scores[n // 2 - 1] + scores[n // 2]) / 2
    )
    perfect = sum(1 for s in scores if s >= 1.0)
    return {
        "n": n,
        "macro_recall": macro,
        "median_recall": median,
        "perfect_count": perfect,
    }
