"""Feature — direct subclass of PhysicalEndurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.physical_endurant import PhysicalEndurant


with core:

    class Feature(PhysicalEndurant):
        """
        A Feature is a physical endurant which has a unity criterion and
        is existentially dependent on another physical endurant, its
        host (examples: a hole, a bump, an object’s boundary, a stain on
        a t-shirt).
        """

    Feature.label = ["Feature"]


__all__ = ["Feature"]
