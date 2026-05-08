"""Stative — direct subclass of Perdurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.perdurant import Perdurant


with core:

    class Stative(Perdurant):
        """
        A Stative is a cumulative perdurant, i.e., a perdurant that when
        summed to another perdurant of the same type, gives a perdurant
        of the same type (examples: sitting, walking, waiting).
        """

    Stative.label = ["Stative"]


__all__ = ["Stative"]
