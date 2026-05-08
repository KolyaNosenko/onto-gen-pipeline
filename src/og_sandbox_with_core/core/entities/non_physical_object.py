"""NonPhysicalObject — direct subclass of NonPhysicalEndurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.non_physical_endurant import NonPhysicalEndurant


with core:

    class NonPhysicalObject(NonPhysicalEndurant):
        """
        A Non-Physical Object is a non-physical endurant with unity
        criterion (examples: a theory, a topic, a concept).
        """

    NonPhysicalObject.label = ["Non-Physical Object"]


__all__ = ["NonPhysicalObject"]
