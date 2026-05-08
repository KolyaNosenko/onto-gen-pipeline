"""Accomplishment — direct subclass of Event."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.event import Event


with core:

    class Accomplishment(Event):
        """
        An Accomplishment is an event which is mereologically non-atomic
        (examples: a conference, an ascent, a performance).
        """

    Accomplishment.label = ["Accomplishment"]


__all__ = ["Accomplishment"]
