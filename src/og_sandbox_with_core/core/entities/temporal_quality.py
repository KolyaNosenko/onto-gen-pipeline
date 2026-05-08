"""TemporalQuality — direct subclass of Quality."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.quality import Quality


with core:

    class TemporalQuality(Quality):
        """
        A Temporal Quality is a quality that directly inheres to a
        perdurant (example: the duration of World War I, the starting
        time of the 2000 Olympics).
        """

    TemporalQuality.label = ["Temporal Quality"]


__all__ = ["TemporalQuality"]
