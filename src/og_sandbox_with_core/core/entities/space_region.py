"""SpaceRegion — direct subclass of PhysicalRegion."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.physical_region import PhysicalRegion


with core:

    class SpaceRegion(PhysicalRegion):
        """
        A Space Region is a physical region, possibly disconnected, for
        spatial locations (examples: the region occupied by Earth in
        this moment, the region where it snowed in the year 1900).
        """

    SpaceRegion.label = ["Space Region"]


__all__ = ["SpaceRegion"]
