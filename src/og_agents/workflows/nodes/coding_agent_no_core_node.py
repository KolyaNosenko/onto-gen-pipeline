from og_agents.coding_agent import MAIN_NO_CORE_TEMPLATE_PATH
from og_agents.prompts import NoCorePrompt
from og_agents.workflows.nodes.coding_agent_node import _BaseCodingAgentNode
from og_agents.sandbox_paths import NO_CORE_ENV_DIR


CODING_AGENT_NO_CORE_NODE_NAME = 'coding_agent_no_core'


class CodingAgentNoCoreNode(_BaseCodingAgentNode):
    _NODE_NAME = CODING_AGENT_NO_CORE_NODE_NAME
    _ENV_DIR = NO_CORE_ENV_DIR
    _MAIN_TEMPLATE = MAIN_NO_CORE_TEMPLATE_PATH
    _DEFAULT_PROMPT_CLS = NoCorePrompt
