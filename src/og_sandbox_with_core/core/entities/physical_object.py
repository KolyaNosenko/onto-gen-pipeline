"""PhysicalObject — direct subclass of PhysicalEndurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.physical_endurant import PhysicalEndurant


with core:

    class PhysicalObject(PhysicalEndurant):
        """
        A Physical Object is a physical endurant with unity criterion
        (examples: a person, a human body, a house, a computer).
        """

    PhysicalObject.label = ["Physical Object"]


__all__ = ["PhysicalObject"]
