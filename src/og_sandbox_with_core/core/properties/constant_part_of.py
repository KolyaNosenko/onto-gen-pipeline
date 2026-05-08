"""constantPartOf — transitive ObjectProperty, subPropertyOf constantlyOverlaps."""

from og_sandbox_with_core.engine import TransitiveProperty
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant
from og_sandbox_with_core.core.properties.constantly_overlaps import constantlyOverlaps


with core:

    class constantPartOf(constantlyOverlaps, TransitiveProperty):
        """
        ConstantPartOf is the constant version of Temporary Parthood
        which is a ternary relation between two endurants x, y and a
        time interval t. The intended interpretation is that the
        endurant x is a part of the endurant y over the time interval
        t.
In this constant version, the endurant x is part of the
        endurant y during the whole existence of y.
        """
        domain = [Endurant]
        range = [Endurant]

    constantPartOf.label = ["constant part of"]


__all__ = ["constantPartOf"]
