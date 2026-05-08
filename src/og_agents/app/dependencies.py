from dataclasses import dataclass

import streamlit as st
from langchain_core.language_models import BaseChatModel
from langgraph.graph.state import CompiledStateGraph

from og_agents.common.http_client import RequestsHttpClient
from og_agents.config import AppConfig
from og_agents.language_models import language_model_factory
from og_agents.ontology.ontology_storage import OntologyStorage
from og_agents.state import GenerationState
from og_agents.workflows import WorkflowContext
from og_agents.workflows.pipelines import full_ui_pipeline
from og_agents.workflows.requests import GenerateOntologyRequest


@dataclass(frozen=True)
class AppDependencies:
    app_config: AppConfig
    ontology_storage: OntologyStorage
    http_client: RequestsHttpClient
    language_model: BaseChatModel
    ontology_generation_workflow: CompiledStateGraph[
        GenerationState, WorkflowContext, GenerateOntologyRequest
    ]


@st.cache_resource
def init_app_dependencies() -> AppDependencies:
    app_config = AppConfig.init()
    return AppDependencies(
        app_config=app_config,
        ontology_storage=OntologyStorage(app_config),
        http_client=RequestsHttpClient(),
        language_model=language_model_factory(app_config),
        ontology_generation_workflow=full_ui_pipeline(app_config),
    )
