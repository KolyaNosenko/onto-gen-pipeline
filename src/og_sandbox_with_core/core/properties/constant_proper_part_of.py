"""constantProperPartOf — transitive ObjectProperty, subPropertyOf constantPartOf."""

from og_sandbox_with_core.engine import TransitiveProperty
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant
from og_sandbox_with_core.core.properties.constant_part_of import constantPartOf


with core:

    class constantProperPartOf(constantPartOf, TransitiveProperty):
        """
        constantProperPartOf is the irreflexive specialization of the
        constantPartOf relation.
        """
        domain = [Endurant]
        range = [Endurant]

    constantProperPartOf.label = ["constant proper part of"]


__all__ = ["constantProperPartOf"]
