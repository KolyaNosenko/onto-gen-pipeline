"""properPartOf — transitive ObjectProperty, subPropertyOf partOf."""

from og_sandbox_with_core.engine import TransitiveProperty, Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.abstract import Abstract
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.properties.part_of import partOf


with core:

    class properPartOf(partOf, TransitiveProperty):
        """
        properPartOf is the irreflexive specialization of the partOf
        relation. (Irreflexivity not captured here, as transitivity is
        favored)
        """
        domain = [Or([Abstract, Perdurant])]
        range = [Or([Abstract, Perdurant])]

    properPartOf.label = ["proper part of"]


__all__ = ["properPartOf"]
