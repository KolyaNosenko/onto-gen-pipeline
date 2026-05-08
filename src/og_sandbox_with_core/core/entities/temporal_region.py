"""TemporalRegion — direct subclass of Region."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.region import Region


with core:

    class TemporalRegion(Region):
        """
        A Temporal Region is a region in a quality space for temporal
        qualities (examples: a time interval, a historical period, a
        velocity).
        """

    TemporalRegion.label = ["Temporal Region"]


__all__ = ["TemporalRegion"]
