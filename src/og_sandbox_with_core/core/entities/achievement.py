"""Achievement — direct subclass of Event."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.event import Event


with core:

    class Achievement(Event):
        """
        An Achievement is an event which is mereologically atomic
        (examples: reaching the summit of K2, a departure, a death).
        """

    Achievement.label = ["Achievement"]


__all__ = ["Achievement"]
