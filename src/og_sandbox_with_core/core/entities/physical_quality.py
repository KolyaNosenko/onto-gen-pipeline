"""PhysicalQuality — direct subclass of Quality."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.quality import Quality


with core:

    class PhysicalQuality(Quality):
        """
        A Physical Quality is a quality that directly inheres to a
        physical endurant (examples: the weight of a pen, the color of
        an apple).
        """

    PhysicalQuality.label = ["Physical Quality"]


__all__ = ["PhysicalQuality"]
