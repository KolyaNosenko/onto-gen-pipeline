
from __future__ import annotations

import json
import logging
import time
import traceback
from typing import Any

from ragas import experiment

from og_evaluation.evals.relation_recall.metrics import relation_recall_metric
from og_evaluation.pipeline_cache import PipelineArtifacts, TtlDiskCache
from og_evaluation.workflows import OntologyGenerationWorkflowFactory
from og_evaluation.workflows.ontology_generation_workflow_factory import (
    CompiledOntologyWorkflow,
)

logger = logging.getLogger(__name__)


def _coerce_list_of_lists(value: Any) -> list[list[str]]:
    if not value:
        return []
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            return []
    return [[str(v) for v in inner] for inner in value]


@experiment()
async def relation_recall_experiment(
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

    head_mentions = _coerce_list_of_lists(row.get("head_mentions"))
    tail_mentions = _coerce_list_of_lists(row.get("tail_mentions"))
    relation_aliases = _coerce_list_of_lists(row.get("relation_aliases"))

    score = await relation_recall_metric.ascore(
        prediction_ttl=prediction_ttl,
        head_mentions=head_mentions,
        tail_mentions=tail_mentions,
        relation_aliases=relation_aliases,
    )

    return {
        "id": row.get("id"),
        "title": row.get("title"),
        "n_gold_triples": len(head_mentions),
        "predicted_ttl_size": len(prediction_ttl),
        "pipeline_status": pipeline_status,
        "failure_traceback": last_traceback,
        "outcome": score.reason,
        "score": score.value,
    }
