"""Particular — top-level concept of the core ontology."""

from og_sandbox_with_core.engine import Thing
from og_sandbox_with_core.core.ontology import core


with core:

    class Particular(Thing):
        """
        A Particular is an entity that cannot have instances, in this
        sense it is opposed to universals (examples: a person, a soccer
        game, a plan, the color red, a feeling, a fact, a theory, number
        forty-two).
        """

    Particular.label = ["Particular"]


__all__ = ["Particular"]
