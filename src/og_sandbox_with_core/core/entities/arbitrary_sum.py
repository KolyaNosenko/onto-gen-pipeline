"""ArbitrarySum — direct subclass of Endurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant


with core:

    class ArbitrarySum(Endurant):
        """
        An Arbitrary Sum is an endurant which is the mereological sum of
        at least a physical and a non-physical endurant.
        """

    ArbitrarySum.label = ["Arbitrary Sum"]


__all__ = ["ArbitrarySum"]
