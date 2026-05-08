from abc import ABC

from langchain_core.prompts import PromptTemplate

from og_agents.coding_agent.coding_agent import RESULT_FILE_NAME


# All coding-agent variants edit `main.py` in the sandbox CWD and
# verify success by running `python main.py` and checking that the
# expected `output.txt` file is non-empty.
_BUILDER_FILE_NAME = "main.py"
_RUN_COMMAND = "python main.py"


class BaseCodingAgentPrompt(ABC):

    _template: PromptTemplate

    def __init__(self, prompt_template: str):
        self._template = PromptTemplate(
            template=prompt_template,
            input_variables=[
                "source_text",
                "competency_questions",
                "builder_file",
                "run_command",
                "result_file",
            ],
            template_format="jinja2",
        )

    def build(self, source_text: str, competency_questions: str | None) -> str:
        return self._template.format(
            source_text=source_text,
            competency_questions=(competency_questions or "").strip(),
            builder_file=_BUILDER_FILE_NAME,
            run_command=_RUN_COMMAND,
            result_file=RESULT_FILE_NAME,
        )
