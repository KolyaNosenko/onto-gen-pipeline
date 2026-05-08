"""Endurant — direct subclass of Particular."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.particular import Particular


with core:

    class Endurant(Particular):
        """
        An Endurant is an entity wholly present, i.e., all its proper
        parts are present, at any time that it is present (examples: a
        person, a tree, an atom, an idea).
        """

    Endurant.label = ["Endurant"]


__all__ = ["Endurant"]
