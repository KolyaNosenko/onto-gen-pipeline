"""Region — direct subclass of Abstract."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.abstract import Abstract


with core:

    class Region(Abstract):
        """
        A Region is an abstract entity classified by a quality type and
        with mereological structure, the sum of all the regions of a
        quality type is called a quality space (examples: the color red
        is a region in the quality space of color, the red of a rose is
        a (sub)region of the red region in the quality space of color,
        the commercial value of 1 Euro is a region in the quality space
        of commercial values).
        """

    Region.label = ["Region"]


__all__ = ["Region"]
