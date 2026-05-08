from og_sandbox_with_core.engine import get_ontology

NS_IRI = "https://og.example.org/ontology"

core = get_ontology(NS_IRI)

__all__ = ["NS_IRI", "core"]
