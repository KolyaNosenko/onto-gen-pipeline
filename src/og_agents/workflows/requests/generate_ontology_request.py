from typing import TypedDict

from og_agents.documents import OntologySourceDocument

class GenerateOntologyRequest(TypedDict, total=False):
    raw_files: list[bytes]
    documents: list[OntologySourceDocument]
