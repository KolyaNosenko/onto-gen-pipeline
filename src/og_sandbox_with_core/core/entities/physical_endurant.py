"""PhysicalEndurant — direct subclass of Endurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant


with core:

    class PhysicalEndurant(Endurant):
        """
        A Physical Endurant is an endurant with direct spatial quality
        (examples: a person, a tree, an atom, the water in a glass, a
        hole in a wall, the center of the Earth).
        """

    PhysicalEndurant.label = ["Physical Endurant"]


__all__ = ["PhysicalEndurant"]
