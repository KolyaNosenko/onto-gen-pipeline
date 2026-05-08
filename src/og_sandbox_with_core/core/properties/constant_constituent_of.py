"""constantConstituentOf — transitive ObjectProperty, subPropertyOf inverseOf(specificallyDependsOn)."""

from og_sandbox_with_core.engine import ObjectProperty, TransitiveProperty, Or
from og_sandbox_with_core.engine.base import (
    owl_inverse_property,
    rdfs_subpropertyof,
)
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.entities.non_physical_endurant import NonPhysicalEndurant
from og_sandbox_with_core.core.entities.physical_endurant import PhysicalEndurant
from og_sandbox_with_core.core.properties.specifically_depends_on import specificallyDependsOn


with core:

    class constantConstituentOf(ObjectProperty, TransitiveProperty):
        """
        constantConstituentOf is the constant version of Constitution
        which is a ternary relation between two endurants x, y and time
        interval t or between two perdurants x, y and time interval t.
        The intended interpretation is that x constitutes y over the
        time interval t.
In this constant version, the entity x
        constitutes y during the whole existence of y.
        """
        domain = [Or([NonPhysicalEndurant, Perdurant, PhysicalEndurant])]
        range = [Or([NonPhysicalEndurant, Perdurant, PhysicalEndurant])]

    constantConstituentOf.label = ["constant constituent of"]


# `subPropertyOf [inverseOf specificallyDependsOn]` — write the bnode
# triple pair directly so round-trip preserves the source axiom.
_inverse_bnode = core.world.new_blank_node()
core._add_obj_triple_spo(
    _inverse_bnode, owl_inverse_property, specificallyDependsOn.storid
)
core._add_obj_triple_spo(
    constantConstituentOf.storid, rdfs_subpropertyof, _inverse_bnode
)


__all__ = ["constantConstituentOf"]
