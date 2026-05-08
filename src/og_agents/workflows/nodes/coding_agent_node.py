from pathlib import Path

from langgraph.runtime import Runtime
from langgraph.config import get_stream_writer

from og_agents.coding_agent import (
    CodingAgent,
    MAIN_TEMPLATE_PATH,
    reset_workspace,
)
from og_agents.config import AppConfig
from og_agents.prompts import BaseCodingAgentPrompt, WithCorePrompt
from og_agents.state import GenerationState
from og_agents.workflows.nodes.base_node import BaseNode
from og_agents.workflows.workflow_context import WorkflowContext
from og_agents.sandbox_paths import WITH_CORE_ENV_DIR

CODING_AGENT_NODE_NAME = 'coding_agent'


class _BaseCodingAgentNode(BaseNode):

    _NODE_NAME: str
    _ENV_DIR: Path
    _MAIN_TEMPLATE: Path
    _DEFAULT_PROMPT_CLS: type[BaseCodingAgentPrompt]

    def __init__(self, config: AppConfig, prompt: BaseCodingAgentPrompt | None = None):
        super().__init__(self._NODE_NAME)
        self._config = config
        self._prompt = prompt or self._DEFAULT_PROMPT_CLS()

    def __call__(
        self, state: GenerationState, runtime: Runtime[WorkflowContext]
    ) -> GenerationState:
        stream_writer = get_stream_writer()

        documents = state.get('documents') or []
        source_text = documents[0].page_content.strip() if documents else ''
        competency_questions = (state.get('competency_questions') or '').strip()

        stream_writer({
            "current_step": self._NODE_NAME,
            'message': 'Початок генерації онтології через код...'
        })
        print('Coding agent source text:', source_text[:200], '...' if len(source_text) > 200 else '')
        print('Coding agent competency questions:', competency_questions[:200], '...' if len(competency_questions) > 200 else '')

        task = self._prompt.build(source_text, competency_questions or None)
        reset_workspace(self._ENV_DIR, main_template=self._MAIN_TEMPLATE)
        coding_agent = CodingAgent.create(self._config)
        result = coding_agent.run(
            task=task,
            workspace=self._ENV_DIR,
            source_text=source_text,
            competency_questions=competency_questions or None,
        )

        print('Coding agent produced Turtle of length:', len(result))
        stream_writer({
            "current_step": self._NODE_NAME,
            'message': 'Онтологію згенеровано через код',
            'ontology_ttl': result,
        })

        return {'ontology_ttl': result}


class CodingAgentNode(_BaseCodingAgentNode):
    _NODE_NAME = CODING_AGENT_NODE_NAME
    _ENV_DIR = WITH_CORE_ENV_DIR
    _MAIN_TEMPLATE = MAIN_TEMPLATE_PATH
    _DEFAULT_PROMPT_CLS = WithCorePrompt
