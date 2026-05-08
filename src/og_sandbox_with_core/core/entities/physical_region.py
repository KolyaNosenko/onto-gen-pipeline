"""PhysicalRegion — direct subclass of Region."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.region import Region


with core:

    class PhysicalRegion(Region):
        """
        A Physical Region is a region in a quality space for physical
        qualities (examples: the physical space, an area in the color
        quality space, 80Kg).
        """

    PhysicalRegion.label = ["Physical Region"]


__all__ = ["PhysicalRegion"]
