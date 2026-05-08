from langgraph.runtime import Runtime
from langgraph.config import get_stream_writer

from og_agents.documents import OntologySourceDocument
from og_agents.state import GenerationState
from og_agents.workflows.nodes.base_node import BaseNode
from og_agents.workflows.workflow_context import WorkflowContext

DOCUMENTS_LOADING_NODE_NAME = "documents_loading"


class DocumentsLoadingNode(BaseNode):

    def __init__(self):
        super().__init__(DOCUMENTS_LOADING_NODE_NAME)

    def __call__(
        self, state: GenerationState, runtime: Runtime[WorkflowContext]
    ) -> GenerationState:
        raw_files = state.get("raw_files") or []
        stream_writer = get_stream_writer()

        if not raw_files:
            stream_writer(
                {
                    "current_step": DOCUMENTS_LOADING_NODE_NAME,
                    "message": "Файлів немає, пропускаю крок.",
                }
            )
            return {}

        stream_writer(
            {
                "current_step": DOCUMENTS_LOADING_NODE_NAME,
                "message": f"Завантаження {len(raw_files)} файлу(ів)...",
            }
        )

        documents = [
            OntologySourceDocument(
                page_content=raw.decode("utf-8", errors="ignore")
            )
            for raw in raw_files
        ]

        stream_writer(
            {
                "current_step": DOCUMENTS_LOADING_NODE_NAME,
                "message": f"Файли завантажено ({len(documents)}).",
            }
        )

        return {"documents": documents}
