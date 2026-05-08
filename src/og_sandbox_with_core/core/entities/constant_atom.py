"""ConstantAtom — direct subclass of Endurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant


with core:

    class ConstantAtom(Endurant):
        """A constant atom is an endurant that has no constant proper parts"""

    ConstantAtom.label = ["Constant Atom"]


__all__ = ["ConstantAtom"]
