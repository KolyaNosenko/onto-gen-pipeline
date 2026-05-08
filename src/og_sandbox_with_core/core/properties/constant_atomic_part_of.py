"""constantAtomicPartOf — ObjectProperty, subPropertyOf constantPartOf."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant
from og_sandbox_with_core.core.entities.constant_atom import ConstantAtom
from og_sandbox_with_core.core.properties.constant_part_of import constantPartOf


with core:

    class constantAtomicPartOf(constantPartOf):
        """
        constantAtomicPartOf is the specialization of the ConstantPartOf
        relation to the case that the part argument is a mereological
        atom
        """
        domain = [ConstantAtom]
        range = [Endurant]

    constantAtomicPartOf.label = ["constant atomic part of"]


__all__ = ["constantAtomicPartOf"]
