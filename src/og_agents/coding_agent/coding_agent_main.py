"""
=== TASK INPUT ===
Source text:
{{SOURCE_TEXT}}

{{COMPETENCY_QUESTIONS}}
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core

# TODO: import the core entity classes you actually subclass.
# Example:
#     from og_sandbox_with_core.core.entities import SocialObject, NonAgentivePhysicalObject

# TODO (optional): import the core properties you actually subclass.
# Example:
#     from og_sandbox_with_core.core.properties import partOf


with core:
    # TODO: declare your domain entity classes here.
    # Each MUST be a subclass of a class from `og_sandbox_with_core.core.entities`
    # (or of another domain class that ultimately roots in one). Direct
    # subclassing of `Thing` is forbidden — pick the most specific core
    # ancestor that fits.

    # TODO: declare your domain ObjectProperty / DataProperty subclasses
    # here. If a core property matches the text's semantics, subclass it;
    # otherwise declare a fresh ObjectProperty / DataProperty with explicit
    # domain / range.

    # TODO: create concrete instances ONLY for named entities the source
    # text mentions by name. Format: name = SomeClass("name_from_text").

    pass  # remove once at least one declaration is added above


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
