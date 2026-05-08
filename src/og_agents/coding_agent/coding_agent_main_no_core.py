"""
=== TASK INPUT ===
Source text:
{{SOURCE_TEXT}}

{{COMPETENCY_QUESTIONS}}
=== END TASK INPUT ===

Domain model entry point (no-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
a fresh `with model:` block and writes the resulting graph to
`output.txt` in this directory.
"""
from og_sandbox_no_core.engine import (
    Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    get_ontology, default_world,
)

model = get_ontology("https://og.example.org/ontology")


with model:
    # TODO: declare your domain entity classes here.
    # Subclass `Thing` for top-level types, or another domain class for
    # specialisations. Build a hierarchy when the text says one type is a
    # kind of another.

    # TODO: declare your domain ObjectProperty / DataProperty subclasses
    # here. Mix in `FunctionalProperty`, `TransitiveProperty`,
    # `SymmetricProperty` when the text supports such behavior.

    # TODO: create concrete instances ONLY for named entities the source
    # text mentions by name. Format: name = SomeClass("name_from_text").

    pass  # remove once at least one declaration is added above


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
