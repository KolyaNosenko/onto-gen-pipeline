
from __future__ import annotations

import logging
import time
import traceback

from ragas import experiment

from og_evaluation.evals.oops.metrics import oops_metric
from og_evaluation.evals.oops.oops_validator_adapter import run_oops
from og_evaluation.pipeline_cache import PipelineArtifacts, TtlDiskCache
from og_evaluation.workflows import OntologyGenerationWorkflowFactory
from og_evaluation.workflows.ontology_generation_workflow_factory import (
    CompiledOntologyWorkflow,
)

logger = logging.getLogger(__name__)


def _serialize_pitfall(pitfall) -> dict:
    return {
        "code": pitfall.code,
        "name": pitfall.name,
        "importance": pitfall.importance,
        "number_affected": pitfall.number_affected,
    }


@experiment()
async def oops_experiment(
    row: dict,
    workflow: CompiledOntologyWorkflow,
    cache: TtlDiskCache,
    retry: int = 0,
):
    text = row["text"]
    last_traceback: str | None = None

    def _compute() -> PipelineArtifacts:
        nonlocal last_traceback
        for attempt in range(retry + 1):
            try:
                artifacts = OntologyGenerationWorkflowFactory.invoke(workflow, text)
            except Exception:  # pylint: disable=broad-except
                last_traceback = traceback.format_exc()
                logger.exception(
                    "workflow.invoke raised on id=%s (attempt %d/%d)",
                    row.get("id"),
                    attempt + 1,
                    retry + 1,
                )
                artifacts = PipelineArtifacts(ttl="")
            if artifacts.ttl:
                return artifacts
            if attempt < retry:
                time.sleep(5 * (2**attempt))
        return PipelineArtifacts(ttl="")

    prediction_ttl = cache.get_or_compute(text, _compute).ttl

    if prediction_ttl:
        pipeline_status = "ok"
    elif last_traceback:
        pipeline_status = "exception"
    else:
        pipeline_status = "empty_ttl"

    if not prediction_ttl:
        return {
            "id": row.get("id"),
            "title": row.get("title"),
            "predicted_ttl_size": 0,
            "pipeline_status": pipeline_status,
            "failure_traceback": last_traceback,
            "oops_outcome": "empty_ttl",
            "criticality_tier": "clean",
            "total_pitfalls": 0,
            "n_critical": 0,
            "n_important": 0,
            "n_minor": 0,
            "pitfall_score_weighted": 0,
            "pitfalls_by_importance": {},
            "pitfalls_by_code": {},
            "total_affected_elements": 0,
            "pitfalls": [],
            "outcome": "skipped: pipeline produced no Turtle",
            "score": 0.0,
        }

    oops_result = run_oops(prediction_ttl)
    score = await oops_metric.ascore(prediction_ttl=prediction_ttl)

    return {
        "id": row.get("id"),
        "title": row.get("title"),
        "predicted_ttl_size": len(prediction_ttl),
        "pipeline_status": pipeline_status,
        "failure_traceback": last_traceback,
        "oops_outcome": oops_result.outcome,
        "criticality_tier": oops_result.criticality_tier(),
        "total_pitfalls": oops_result.total_pitfalls,
        "n_critical": oops_result.n_critical(),
        "n_important": oops_result.n_important(),
        "n_minor": oops_result.n_minor(),
        "pitfall_score_weighted": oops_result.weighted_pitfall_score(),
        "pitfalls_by_importance": oops_result.count_by_importance(),
        "pitfalls_by_code": oops_result.count_by_code(),
        "total_affected_elements": oops_result.total_affected_elements(),
        "pitfalls": [_serialize_pitfall(p) for p in oops_result.pitfalls],
        "outcome": score.reason,
        "score": score.value,
    }
