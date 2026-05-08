"""State — direct subclass of Stative."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.stative import Stative


with core:

    class State(Stative):
        """
        A State is a stative perdurant such that all its parts are of
        the same type (examples: being sitting, being open, being happy,
        being red).
        """

    State.label = ["State"]


__all__ = ["State"]
