"""Society — direct subclass of AgentiveSocialObject."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.agentive_social_object import AgentiveSocialObject


with core:

    class Society(AgentiveSocialObject):
        """
        A Society is a collective agentive social object (examples: a
        nation, the FCA Group, Apple, the European Central Bank).
        """

    Society.label = ["Society"]


__all__ = ["Society"]
