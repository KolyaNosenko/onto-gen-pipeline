"""NonAgentiveSocialObject — direct subclass of SocialObject."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.social_object import SocialObject


with core:

    class NonAgentiveSocialObject(SocialObject):
        """
        A Non-Agentive Social Object is a social object to which
        intentions, believes and desires are not ascribed (examples: a
        law, an economic system, a currency, an asset).
        """

    NonAgentiveSocialObject.label = ["Non-Agentive Social Object"]


__all__ = ["NonAgentiveSocialObject"]
