
from __future__ import annotations

import logging
import time
import traceback

from ragas import experiment

from og_evaluation.evals.structural.metrics import structural_metric
from og_evaluation.evals.structural.ontology_counts import count_structural
from og_evaluation.pipeline_cache import PipelineArtifacts, TtlDiskCache
from og_evaluation.workflows import OntologyGenerationWorkflowFactory
from og_evaluation.workflows.ontology_generation_workflow_factory import (
    CompiledOntologyWorkflow,
)

logger = logging.getLogger(__name__)


_EMPTY_COUNTS: dict = {
    "n_classes": 0,
    "n_object_properties": 0,
    "n_data_properties": 0,
    "n_annotation_properties": 0,
    "n_properties": 0,
    "n_non_is_a_properties": 0,
    "n_individuals": 0,
    "n_subclass_axioms": 0,
    "n_axioms": 0,
    "n_classes_with_instances": 0,
    "n_classes_with_multiple_parents": 0,
    "n_data_property_domain_triples": 0,
    "n_root_classes": 0,
    "n_leaf_classes": 0,
    "n_orphan_classes": 0,
    "n_taxonomy_components": 0,
    "has_taxonomy_cycle": False,
    "n_cycle_classes": 0,
    "max_taxonomy_depth": None,
    "max_taxonomy_breadth": None,
    "relationship_richness": None,
    "inheritance_richness": None,
    "attribute_richness": None,
    "class_richness": None,
    "average_population": None,
    "mean_taxonomy_depth": None,
    "tangledness": None,
}


@experiment()
async def structural_experiment(
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
        score = await structural_metric.ascore(prediction_ttl="")
        return {
            "id": row.get("id"),
            "title": row.get("title"),
            "predicted_ttl_size": 0,
            "pipeline_status": pipeline_status,
            "failure_traceback": last_traceback,
            **_EMPTY_COUNTS,
            "outcome": score.reason,
            "score": score.value,
        }

    counts = count_structural(prediction_ttl)
    score = await structural_metric.ascore(prediction_ttl=prediction_ttl)
    counts_dict = counts.as_dict() if counts is not None else _EMPTY_COUNTS

    return {
        "id": row.get("id"),
        "title": row.get("title"),
        "predicted_ttl_size": len(prediction_ttl),
        "pipeline_status": pipeline_status,
        "failure_traceback": last_traceback,
        **counts_dict,
        "outcome": score.reason,
        "score": score.value,
    }
