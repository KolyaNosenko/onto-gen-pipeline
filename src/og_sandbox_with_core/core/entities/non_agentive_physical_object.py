"""NonAgentivePhysicalObject — direct subclass of PhysicalObject."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.physical_object import PhysicalObject


with core:

    class NonAgentivePhysicalObject(PhysicalObject):
        """
        A Non-Agentive Physical Object is a physical object to which
        intentions, believes and desires are not ascribed (examples: a
        pebble, a house, a computer, a human body).
        """

    NonAgentivePhysicalObject.label = ["Non-Agentive Physical Object"]


__all__ = ["NonAgentivePhysicalObject"]
