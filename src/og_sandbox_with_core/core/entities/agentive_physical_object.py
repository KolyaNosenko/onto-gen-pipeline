"""AgentivePhysicalObject — direct subclass of PhysicalObject."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.physical_object import PhysicalObject


with core:

    class AgentivePhysicalObject(PhysicalObject):
        """
        An Agentive Physical Object is a physical object to which
        intentions, believes and desires are ascribed (examples: a human
        person as opposed to a legal person).
        """

    AgentivePhysicalObject.label = ["Agentive Physical Object"]


__all__ = ["AgentivePhysicalObject"]
