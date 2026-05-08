
from __future__ import annotations

from collections import Counter
from typing import Iterable

from ragas import Experiment
from ragas.metrics import numeric_metric
from ragas.metrics.result import MetricResult

from og_evaluation.evals.consistency.reasoner import check_consistency


@numeric_metric(name="consistency", allowed_values=(0.0, 1.0))
def consistency_metric(prediction_ttl: str) -> MetricResult:
    result = check_consistency(prediction_ttl)
    score = 1.0 if result.is_clean else 0.0
    reason = (
        f"{result.outcome}: classes={result.n_classes}, "
        f"individuals={result.n_individuals}, "
        f"unsatisfiable={result.n_unsatisfiable}"
    )
    if result.error:
        reason += f"; error={result.error[:120]}"
    return MetricResult(value=score, reason=reason)


def calculate_consistency_summary(
    experiment_results: Experiment | Iterable[dict],
) -> dict:
    rows = list(experiment_results)
    n = len(rows)
    if n == 0:
        return {
            "n": 0,
            "consistency_rate": 0.0,
            "outcome_distribution": {},
            "mean_unsatisfiable": 0.0,
            "mean_classes": 0.0,
        }
    consistent = sum(1 for r in rows if float(r.get("score", 0.0)) >= 1.0)
    outcomes = Counter(r.get("reasoner_outcome", "unknown") for r in rows)
    unsat = [int(r.get("n_unsatisfiable", 0) or 0) for r in rows]
    classes = [int(r.get("n_classes", 0) or 0) for r in rows]
    return {
        "n": n,
        "consistency_rate": consistent / n,
        "outcome_distribution": dict(outcomes),
        "mean_unsatisfiable": sum(unsat) / n,
        "mean_classes": sum(classes) / n,
    }
