"""TemporalLocation — direct subclass of TemporalQuality."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.temporal_quality import TemporalQuality


with core:

    class TemporalLocation(TemporalQuality):
        """
        A Temporal Location is a temporal quality of a perdurant and is
        specific to that perdurant, that is, two concurrent perdurants
        have distinct temporal locations. The temporal location is the
        temporal quality which has as quale the unique time interval at
        which the perdurant is exactly located (examples: the temporal
        location of World War I, the temporal location of the
        Anderssen-Kieseritzky chess play in 1851, the temporal location
        of the summers of the 20th century).
        """

    TemporalLocation.label = ["Temporal Location"]


__all__ = ["TemporalLocation"]
