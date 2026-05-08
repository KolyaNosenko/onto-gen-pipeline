from typing import Callable

from langgraph.graph.state import CompiledStateGraph

from og_agents.config import AppConfig
from og_agents.state import GenerationState
from og_agents.workflows.nodes import (
    BaseNode,
    CodingAgentNoCoreNode,
    CodingAgentNode,
    DocumentsLoadingNode,
    GenerateCompetencyQuestionsNode,
    GenerateOntologyNode,
    OOPSOntologyValidationNode,
    OntologyConsistencyValidationNode,
    OntologyRDFSyntaxValidationNode,
    SaveOntologyNode,
)
from og_agents.workflows.ontology_generation_workflow_builder import (
    OntologyGenerationWorkflowBuilder,
)
from og_agents.workflows.requests import GenerateOntologyRequest
from og_agents.workflows.workflow_context import WorkflowContext

CompiledOntologyWorkflow = CompiledStateGraph[
    GenerationState, WorkflowContext, GenerateOntologyRequest
]

PipelineFactory = Callable[..., CompiledOntologyWorkflow]


def _maybe_cq(use_cq: bool) -> list[BaseNode]:
    return [GenerateCompetencyQuestionsNode()] if use_cq else []


def legacy_llm_pipeline(
    config: AppConfig, *, use_cq: bool = True
) -> CompiledOntologyWorkflow:
    nodes: list[BaseNode] = _maybe_cq(use_cq) + [
        GenerateOntologyNode(),
        OntologyRDFSyntaxValidationNode(),
    ]
    return OntologyGenerationWorkflowBuilder.of(nodes).build()


def coding_no_core_pipeline(
    config: AppConfig, *, use_cq: bool = True
) -> CompiledOntologyWorkflow:
    nodes: list[BaseNode] = _maybe_cq(use_cq) + [CodingAgentNoCoreNode(config)]
    return OntologyGenerationWorkflowBuilder.of(nodes).build()


def coding_with_core_pipeline(
    config: AppConfig, *, use_cq: bool = True
) -> CompiledOntologyWorkflow:
    nodes: list[BaseNode] = _maybe_cq(use_cq) + [CodingAgentNode(config)]
    return OntologyGenerationWorkflowBuilder.of(nodes).build()


def full_ui_pipeline(config: AppConfig) -> CompiledOntologyWorkflow:
    return OntologyGenerationWorkflowBuilder.of(
        [
            DocumentsLoadingNode(),
            GenerateCompetencyQuestionsNode(),
            GenerateOntologyNode(),
            OntologyRDFSyntaxValidationNode(),
            OOPSOntologyValidationNode(),
            OntologyConsistencyValidationNode(),
            SaveOntologyNode(),
        ]
    ).build()


PIPELINE_REGISTRY: dict[str, PipelineFactory] = {
    "legacy_llm": legacy_llm_pipeline,
    "coding_no_core": coding_no_core_pipeline,
    "coding_with_core": coding_with_core_pipeline,
}


__all__ = [
    "PipelineFactory",
    "CompiledOntologyWorkflow",
    "legacy_llm_pipeline",
    "coding_no_core_pipeline",
    "coding_with_core_pipeline",
    "full_ui_pipeline",
    "PIPELINE_REGISTRY",
]
