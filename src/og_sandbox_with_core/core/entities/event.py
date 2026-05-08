"""Event — direct subclass of Perdurant."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.perdurant import Perdurant


with core:

    class Event(Perdurant):
        """
        An Event is an anti-cumulative perdurant, i.e., a perdurant that
        when summed to another perdurant of the same type, gives a
        perdurant of a different type (examples: closing a door,
        reaching the top of a mountain, breaking a seal).
        """

    Event.label = ["Event"]


__all__ = ["Event"]
