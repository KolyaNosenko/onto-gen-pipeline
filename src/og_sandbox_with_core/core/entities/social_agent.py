"""SocialAgent — direct subclass of AgentiveSocialObject."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.agentive_social_object import AgentiveSocialObject


with core:

    class SocialAgent(AgentiveSocialObject):
        """
        A Social Agent is an individual agentive social object
        (examples: a teacher, a president, a software agent).
        """

    SocialAgent.label = ["Social Agent"]


__all__ = ["SocialAgent"]
