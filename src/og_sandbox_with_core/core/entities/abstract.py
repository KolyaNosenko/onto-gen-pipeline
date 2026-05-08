"""Abstract — direct subclass of Particular."""
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.particular import Particular


with core:

    class Abstract(Particular):
        """
        An Abstract entity is an entity that has neither spatial nor
        temporal qualities and is not a quality itself (examples: a
        number, a set, a quality space).
        """

    Abstract.label = ["Abstract"]


__all__ = ["Abstract"]
