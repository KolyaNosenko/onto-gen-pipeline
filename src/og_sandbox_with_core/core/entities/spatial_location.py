"""SpatialLocation — direct subclass of PhysicalQuality."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.physical_quality import PhysicalQuality


with core:

    class SpatialLocation(PhysicalQuality):
        """
        A Spatial Location is the individual spatial quality of a
        physical endurant (examples: the spatial quality of the Earth,
        the spatial quality of a hole, the spatial quality of Adolf
        Anderssen).
        """

    SpatialLocation.label = ["Spatial Location"]


__all__ = ["SpatialLocation"]
