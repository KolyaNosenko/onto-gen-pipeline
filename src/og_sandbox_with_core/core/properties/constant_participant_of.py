"""constantParticipantOf — ObjectProperty, subPropertyOf inverseOf(specificallyDependsOn)."""

from og_sandbox_with_core.engine import ObjectProperty
from og_sandbox_with_core.engine.base import (
    owl_inverse_property,
    rdfs_subpropertyof,
)
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.properties.specifically_depends_on import specificallyDependsOn


with core:

    class constantParticipantOf(ObjectProperty):
        """
        constantParticipantOf is the constant version of Participation
        which is a ternary relation between an endurant x, a perdurant
        y, and a time interval t. The intended interpretation is that x
        participates in y at time t. Every perdurant has at least an
        endurant that participates in it, and every endurant
        participates in some perdurant. 
In this constant version, the
        endurant x participates in the perdurant y during the whole
        existence of y.
        """
        domain = [Endurant]
        range = [Perdurant]

    constantParticipantOf.label = ["constant participation of"]


# `subPropertyOf [inverseOf specificallyDependsOn]` — see constant_constituent_of.py
# for rationale.
_inverse_bnode = core.world.new_blank_node()
core._add_obj_triple_spo(
    _inverse_bnode, owl_inverse_property, specificallyDependsOn.storid
)
core._add_obj_triple_spo(
    constantParticipantOf.storid, rdfs_subpropertyof, _inverse_bnode
)


__all__ = ["constantParticipantOf"]
