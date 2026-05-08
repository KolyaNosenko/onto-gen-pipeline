"""atomicPartOf — ObjectProperty, subPropertyOf partOf."""

from og_sandbox_with_core.engine import Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.atom import Atom
from og_sandbox_with_core.core.entities.abstract import Abstract
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.properties.part_of import partOf


with core:

    class atomicPartOf(partOf):
        """
        atomicPartOf is the specialization of the PartOf relation to the
        case that the part argument is a mereological atom
        """
        domain = [Atom]
        range = [Or([Abstract, Perdurant])]

    atomicPartOf.label = ["atomic part of"]


__all__ = ["atomicPartOf"]
