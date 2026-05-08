"""Process — direct subclass of Stative."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.stative import Stative


with core:

    class Process(Stative):
        """
        A Process is a stative perdurant such that at some temporal
        scale some parts are of a different type  (examples: running,
        writing).
        """

    Process.label = ["Process"]


__all__ = ["Process"]
