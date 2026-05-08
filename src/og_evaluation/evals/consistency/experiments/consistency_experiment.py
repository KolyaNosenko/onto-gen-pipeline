
from __future__ import annotations

import logging
import time
import traceback

from ragas import experiment

from og_evaluation.evals.consistency.metrics import consistency_metric
from og_evaluation.evals.consistency.reasoner import check_consistency
from og_evaluation.pipeline_cache import PipelineArtifacts, TtlDiskCache
from og_evaluation.workflows import OntologyGenerationWorkflowFactory
from og_evaluation.workflows.ontology_generation_workflow_factory import (
    CompiledOntologyWorkflow,
)

logger = logging.getLogger(__name__)


@experiment()
async def consistency_experiment(
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

    # Skip the reasoner if the pipeline failed — there is nothing to check.
    if not prediction_ttl:
        return {
            "id": row.get("id"),
            "title": row.get("title"),
            "predicted_ttl_size": 0,
            "pipeline_status": pipeline_status,
            "failure_traceback": last_traceback,
            "reasoner_outcome": "empty_ttl",
            "reasoner_is_consistent": False,
            "n_classes": 0,
            "n_individuals": 0,
            "n_unsatisfiable": 0,
            "reasoning_time_s": 0.0,
            "outcome": "skipped: pipeline produced no Turtle",
            "score": 0.0,
        }

    reasoner_result = check_consistency(prediction_ttl)
    score = await consistency_metric.ascore(prediction_ttl=prediction_ttl)

    return {
        "id": row.get("id"),
        "title": row.get("title"),
        "predicted_ttl_size": len(prediction_ttl),
        "pipeline_status": pipeline_status,
        "failure_traceback": last_traceback,
        "reasoner_outcome": reasoner_result.outcome,
        "reasoner_is_consistent": reasoner_result.is_consistent,
        "n_classes": reasoner_result.n_classes,
        "n_individuals": reasoner_result.n_individuals,
        "n_unsatisfiable": reasoner_result.n_unsatisfiable,
        "reasoning_time_s": reasoner_result.reasoning_time_s,
        "unsatisfiable_iris": reasoner_result.unsatisfiable_iris,
        "outcome": score.reason,
        "score": score.value,
    }
