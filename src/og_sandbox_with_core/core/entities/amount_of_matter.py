"""AmountOfMatter — direct subclass of PhysicalEndurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.physical_endurant import PhysicalEndurant


with core:

    class AmountOfMatter(PhysicalEndurant):
        """
        An Amount Of Matter is a physical endurant which has no unity
        criterion and is mereologically invariant, that is, all its part
        are essential parts (examples: the gold of my wedding ring, the
        sand used to make this glass).
        """

    AmountOfMatter.label = ["Amount of Matter"]


__all__ = ["AmountOfMatter"]
