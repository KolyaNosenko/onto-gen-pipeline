"""SocialObject — direct subclass of NonPhysicalObject."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.non_physical_object import NonPhysicalObject


with core:

    class SocialObject(NonPhysicalObject):
        """
        A Social Object is a non-physical object which is generically
        dependent on a community of agents (examples: a person in the
        legal sense, a client, a law, an economic system).
        """

    SocialObject.label = ["Social Object"]


__all__ = ["SocialObject"]
