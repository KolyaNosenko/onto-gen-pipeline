"""NonPhysicalEndurant — direct subclass of Endurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant


with core:

    class NonPhysicalEndurant(Endurant):
        """
        A Non-Physical Endurant is an endurant with no direct spatial
        quality (examples: democracy, the United Nations, the general
        secretary of Amnesty International).
        """

    NonPhysicalEndurant.label = ["Non-Physical Endurant"]


__all__ = ["NonPhysicalEndurant"]
