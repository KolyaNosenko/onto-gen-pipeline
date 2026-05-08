
from __future__ import annotations

from collections import Counter
from typing import Iterable

from ragas import Experiment
from ragas.metrics import numeric_metric
from ragas.metrics.result import MetricResult

from og_evaluation.evals.oops.oops_validator_adapter import (
    CriticalityTier,
    run_oops,
)


_TIER_SCORES: dict[CriticalityTier, float] = {
    "clean": 1.00,
    "minor_only": 0.66,
    "important": 0.33,
    "critical": 0.00,
}


@numeric_metric(name="oops_pitfalls", allowed_values=(0.0, 1.0))
def oops_metric(prediction_ttl: str) -> MetricResult:
    result = run_oops(prediction_ttl)
    if result.outcome == "empty_ttl":
        return MetricResult(value=0.0, reason="skipped: empty TTL")
    if result.outcome == "validator_error":
        return MetricResult(
            value=0.0,
            reason=(
                f"validator_error: {result.error[:120] if result.error else ''}"
            ),
        )

    tier = result.criticality_tier()
    score = _TIER_SCORES[tier]
    if tier == "clean":
        reason = "no pitfalls"
    else:
        reason = (
            f"tier={tier}; "
            f"critical={result.n_critical()} "
            f"important={result.n_important()} "
            f"minor={result.n_minor()} "
            f"(total={result.total_pitfalls}, "
            f"weighted={result.weighted_pitfall_score()}); "
            f"by_code={result.count_by_code()}"
        )
    return MetricResult(value=score, reason=reason)


def calculate_oops_summary(
    experiment_results: Experiment | Iterable[dict],
) -> dict:
    rows = list(experiment_results)
    n = len(rows)
    if n == 0:
        return {
            "n": 0,
            "clean_rate": 0.0,
            "critical_clean_rate": 0.0,
            "important_clean_rate": 0.0,
            "outcome_distribution": {},
            "tier_distribution": {},
            "mean_pitfalls": 0.0,
            "mean_critical": 0.0,
            "mean_important": 0.0,
            "mean_minor": 0.0,
            "mean_pitfall_score_weighted": 0.0,
            "pitfalls_by_code": {},
            "pitfalls_by_importance": {},
        }

    code_totals: Counter[str] = Counter()
    importance_totals: Counter[str] = Counter()
    outcome_counts: Counter[str] = Counter()
    tier_counts: Counter[str] = Counter()
    pitfall_counts: list[int] = []
    critical_counts: list[int] = []
    important_counts: list[int] = []
    minor_counts: list[int] = []
    weighted_scores: list[int] = []

    for row in rows:
        outcome_counts[row.get("oops_outcome", "unknown")] += 1
        tier_counts[row.get("criticality_tier", "unknown")] += 1
        pitfall_counts.append(int(row.get("total_pitfalls", 0) or 0))
        critical_counts.append(int(row.get("n_critical", 0) or 0))
        important_counts.append(int(row.get("n_important", 0) or 0))
        minor_counts.append(int(row.get("n_minor", 0) or 0))
        weighted_scores.append(
            int(row.get("pitfall_score_weighted", 0) or 0)
        )
        for code, count in (row.get("pitfalls_by_code") or {}).items():
            code_totals[code] += int(count)
        for imp, count in (row.get("pitfalls_by_importance") or {}).items():
            importance_totals[imp] += int(count)

    clean = sum(1 for r in rows if float(r.get("score", 0.0)) >= 1.0)
    critical_clean = sum(1 for c in critical_counts if c == 0)
    important_clean = sum(
        1 for c, i in zip(critical_counts, important_counts) if c == 0 and i == 0
    )

    return {
        "n": n,
        "clean_rate": clean / n,
        "critical_clean_rate": critical_clean / n,
        "important_clean_rate": important_clean / n,
        "outcome_distribution": dict(outcome_counts),
        "tier_distribution": dict(tier_counts),
        "mean_pitfalls": sum(pitfall_counts) / n,
        "mean_critical": sum(critical_counts) / n,
        "mean_important": sum(important_counts) / n,
        "mean_minor": sum(minor_counts) / n,
        "mean_pitfall_score_weighted": sum(weighted_scores) / n,
        "pitfalls_by_code": dict(code_totals.most_common()),
        "pitfalls_by_importance": dict(importance_totals.most_common()),
    }
