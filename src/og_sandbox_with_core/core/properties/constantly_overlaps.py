"""constantlyOverlaps — symmetric ObjectProperty over Endurant."""

from og_sandbox_with_core.engine import ObjectProperty, SymmetricProperty
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant


with core:

    class constantlyOverlaps(ObjectProperty, SymmetricProperty):
        """
        constantlyOverlaps holds between two endurants that share a
        constant part, and are such that the time intervals at which
        they are temporally located overlap.
        """
        domain = [Endurant]
        range = [Endurant]

    constantlyOverlaps.label = ["constantly overlaps"]


__all__ = ["constantlyOverlaps"]
