"""Perdurant — direct subclass of Particular."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.particular import Particular


with core:

    class Perdurant(Particular):
        """
        A Perdurant is an entity that happens in time (examples: a
        person’s life, a soccer game, the reading of a book, the state
        of feeling happy). Some perdurants are temporally atomic
        (example: the change of a letter’s state due to the breaking of
        the seal).
        """

    Perdurant.label = ["Perdurant"]


__all__ = ["Perdurant"]
