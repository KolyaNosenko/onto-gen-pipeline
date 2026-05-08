"""AgentiveSocialObject — direct subclass of SocialObject."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.social_object import SocialObject


with core:

    class AgentiveSocialObject(SocialObject):
        """
        An Agentive Social Object is a social object to which
        intentions, believes and desires are ascribed (examples: a
        teacher, a president, a software agent, a nation).
        """

    AgentiveSocialObject.label = ["Agentive Social Object"]


__all__ = ["AgentiveSocialObject"]
