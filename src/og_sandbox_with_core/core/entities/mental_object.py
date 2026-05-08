"""MentalObject — direct subclass of NonPhysicalObject."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.non_physical_object import NonPhysicalObject


with core:

    class MentalObject(NonPhysicalObject):
        """
        A Mental Object is a non-physical object which existentially
        depends on an agentive physical object (examples: a percept, a
        sense datum).
        """

    MentalObject.label = ["Mental Object"]


__all__ = ["MentalObject"]
