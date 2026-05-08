from rdflib import Graph

from og_agents.common.http_client import RequestsHttpClient
from og_agents.config import AppConfig
from og_agents.documents import OntologySourceDocument
from og_agents.language_models import language_model_factory
from og_agents.ontology import OntologyStorage
from og_agents.workflows import WorkflowContext
from og_agents.workflows.pipelines import coding_with_core_pipeline

SAMPLE_TEXT = (
    "The saxophone is a family of woodwind instruments invented by the Belgian "
    "instrument maker Adolphe Sax in 1846. A saxophone has a mouthpiece with a "
    "single reed, a conical metal body, and finger keys. Saxophones are classified "
    "by pitch range: the soprano saxophone, the alto saxophone, the tenor saxophone, "
    "and the baritone saxophone are the most common. Although the body is made of "
    "metal (typically brass), saxophones are considered woodwind instruments because "
    "sound is produced by a vibrating reed. Saxophones are widely used in jazz, "
    "classical and military band music."
)


def main():
    config = AppConfig.init()
    http_client = RequestsHttpClient()

    workflow = coding_with_core_pipeline(config)
    language_model = language_model_factory(config)
    ontology_storage = OntologyStorage(config)

    result_state = workflow.invoke(
        {
            'documents': [
                OntologySourceDocument(page_content=SAMPLE_TEXT),
            ]
        },
        context=WorkflowContext(
            config=config,
            http_client=http_client,
            language_model=language_model,
            ontology_storage=ontology_storage,
        ),
    )

    ontology_ttl = result_state.get('ontology_ttl') or ''
    preview_len = min(len(ontology_ttl), 600)

    print("=" * 60)
    print("Pipeline finished.")
    print(f"ontology_ttl length: {len(ontology_ttl)} chars")
    print("--- first", preview_len, "chars ---")
    print(ontology_ttl[:preview_len])
    print("--- end preview ---")

    graph = Graph()
    graph.parse(data=ontology_ttl, format="turtle")
    print(f"parsed triples: {len(graph)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
