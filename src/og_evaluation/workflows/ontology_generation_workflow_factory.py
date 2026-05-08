
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from langgraph.graph.state import CompiledStateGraph

from og_agents.common.http_client import RequestsHttpClient
from og_agents.config import AppConfig
from og_agents.documents import OntologySourceDocument
from og_agents.language_models import language_model_factory
from og_agents.ontology import OntologyStorage
from og_agents.sandbox_paths import NO_CORE_ENV_DIR, WITH_CORE_ENV_DIR
from og_agents.workflows import WorkflowContext
from og_agents.workflows.pipelines import PIPELINE_REGISTRY

from og_evaluation.pipeline_cache import PipelineArtifacts


DEFAULT_VARIANT = "coding_with_core"

# Coding-agent variants leave their generated `main.py` in a fixed
# workspace; we read it after each invocation so it can be cached
# alongside the resulting Turtle.
_VARIANT_WORKSPACES: dict[str, Path] = {
    "coding_with_core": WITH_CORE_ENV_DIR,
    "coding_no_core": NO_CORE_ENV_DIR,
}


@dataclass
class CompiledOntologyWorkflow:
    workflow: CompiledStateGraph
    context: WorkflowContext
    variant: str


class OntologyGenerationWorkflowFactory:
    @staticmethod
    def create(
        *,
        language_model_name: str | None = None,
        model_provider_api_key: str | None = None,
        variant: str = DEFAULT_VARIANT,
        use_cq: bool = True,
    ) -> CompiledOntologyWorkflow:
        if variant not in PIPELINE_REGISTRY:
            raise ValueError(
                f"Unknown pipeline variant {variant!r}. Available: {sorted(PIPELINE_REGISTRY)}"
            )

        app_config = AppConfig(
            language_model_name=language_model_name,
            model_provider_api_key=model_provider_api_key,
        )
        factory = PIPELINE_REGISTRY[variant]
        workflow = factory(app_config, use_cq=use_cq)
        context = WorkflowContext(
            config=app_config,
            http_client=RequestsHttpClient(),
            language_model=language_model_factory(app_config),
            ontology_storage=OntologyStorage(app_config),
        )
        return CompiledOntologyWorkflow(
            workflow=workflow, context=context, variant=variant
        )

    @staticmethod
    def invoke(
        compiled: CompiledOntologyWorkflow, scenario_text: str
    ) -> PipelineArtifacts:
        result_state = compiled.workflow.invoke(
            input={
                "documents": [OntologySourceDocument(page_content=scenario_text)],
            },
            context=compiled.context,
        )
        ttl = (result_state or {}).get("ontology_ttl") or ""
        main_py = _read_main_py(compiled.variant)
        return PipelineArtifacts(ttl=ttl, main_py=main_py)


def _read_main_py(variant: str) -> str | None:
    workspace = _VARIANT_WORKSPACES.get(variant)
    if workspace is None:
        return None
    main_py_path = workspace / "main.py"
    if not main_py_path.exists():
        return None
    return main_py_path.read_text(encoding="utf-8")
