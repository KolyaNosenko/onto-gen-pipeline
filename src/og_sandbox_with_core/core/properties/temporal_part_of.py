"""temporalPartOf — transitive ObjectProperty, subPropertyOf partOf."""

from og_sandbox_with_core.engine import TransitiveProperty
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.properties.part_of import partOf


with core:

    class temporalPartOf(partOf, TransitiveProperty):
        """
        temporalPartOf is the specialisation of the partOf relation
        between two perdurants x and y, x being a temporal slice of y,
        that is, a maximal part of y during some time interval.
        """
        domain = [Perdurant]
        range = [Perdurant]

    temporalPartOf.label = ["temporal part of"]


__all__ = ["temporalPartOf"]
