"""Property chain axioms (`owl:propertyChainAxiom`).

Each chain is materialised as a fresh rdf:List blank node attached to its
target property. Anonymous `inverseOf` components become their own blank
nodes ``[ owl:inverseOf <P> ]``. We bypass owlready2's ``PropertyChain``
class because the forked engine has known issues with chains that include
``Inverse(...)`` components — see the failed paths in
``engine/class_construct.py:_set_ontology_copy_if_needed``. The low-level
triple writer below produces faithful round-trip output without going
through that code path.

Each call to ``add_chain`` is preceded by a Python comment with the source
``rdfs:comment`` (axiom annotation) so a reader sees the rationale next to
the chain.
"""

from og_sandbox_with_core.engine import Inverse
from og_sandbox_with_core.engine.base import (
    owl_inverse_property,
    owl_propertychain,
    rdf_first,
    rdf_nil,
    rdf_rest,
)
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.properties.constant_atomic_part_of import constantAtomicPartOf
from og_sandbox_with_core.core.properties.constant_constituent_of import constantConstituentOf
from og_sandbox_with_core.core.properties.constant_part_of import constantPartOf
from og_sandbox_with_core.core.properties.constant_participant_of import constantParticipantOf
from og_sandbox_with_core.core.properties.constant_proper_part_of import constantProperPartOf
from og_sandbox_with_core.core.properties.constantly_overlaps import constantlyOverlaps
from og_sandbox_with_core.core.properties.direct_quality_of import directQualityOf
from og_sandbox_with_core.core.properties.overlaps import overlaps
from og_sandbox_with_core.core.properties.part_of import partOf
from og_sandbox_with_core.core.properties.present_at import presentAt
from og_sandbox_with_core.core.properties.specifically_depends_on import specificallyDependsOn
from og_sandbox_with_core.core.properties.temporally_located_at import temporallyLocatedAt


def _component_storid(component):
    """Return the storid to use as an rdf:List item for a chain component.

    Named properties contribute their own storid. ``Inverse(prop)`` becomes
    a fresh blank node carrying ``owl:inverseOf <prop>``.
    """
    if isinstance(component, Inverse):
        bnode = core.world.new_blank_node()
        core._add_obj_triple_spo(
            bnode, owl_inverse_property, component.property.storid
        )
        return bnode
    return component.storid


def add_chain(target_prop, components):
    """Append ``owl:propertyChainAxiom (components...)`` to ``target_prop``."""
    storids = [_component_storid(c) for c in components]
    head_bnode = core.world.new_blank_node()
    cur = head_bnode
    for i, storid in enumerate(storids):
        core._add_obj_triple_spo(cur, rdf_first, storid)
        if i < len(storids) - 1:
            nxt = core.world.new_blank_node()
            core._add_obj_triple_spo(cur, rdf_rest, nxt)
            cur = nxt
        else:
            core._add_obj_triple_spo(cur, rdf_rest, rdf_nil)
    core._add_obj_triple_spo(
        target_prop.storid, owl_propertychain, head_bnode
    )


# ---------------------------------------------------------------------------
# Chains on `overlaps`
# ---------------------------------------------------------------------------

# E-1. Inverse(partOf) ∘ partOf → overlaps.
#      "If X has something that is part of Y as part then X overlaps Y."
#      Source rdfs:comment: "D15 (half)"
add_chain(overlaps, [Inverse(partOf, simplify=False), partOf])

# E-2. Inverse(presentAt) ∘ temporallyLocatedAt → overlaps.
#      "If X is a time of presence of something which is temporally located
#       at Y then X overlaps Y."
#      Source rdfs:comment: "Approximation of half of Dd40"
add_chain(overlaps, [Inverse(presentAt, simplify=False), temporallyLocatedAt])


# ---------------------------------------------------------------------------
# Chains on `constantlyOverlaps`
# ---------------------------------------------------------------------------

# E-3. Inverse(constantPartOf) ∘ constantPartOf → constantlyOverlaps.
#      "If X has something that is a constant part of Y as constant part
#       then X constantly overlaps Y."
add_chain(
    constantlyOverlaps,
    [Inverse(constantPartOf, simplify=False), constantPartOf],
)


# ---------------------------------------------------------------------------
# Chains on `presentAt` (10 chains)
# ---------------------------------------------------------------------------

# E-4. constantAtomicPartOf ∘ presentAt → presentAt.
#      "If X is constant atomic part of something that is present at Y
#       then X is present at Y."
add_chain(presentAt, [constantAtomicPartOf, presentAt])

# E-5. constantConstituentOf ∘ presentAt → presentAt.
#      "If X is constant constituent of something that is present at Y
#       then X is present at Y."
add_chain(presentAt, [constantConstituentOf, presentAt])

# E-6. constantPartOf ∘ presentAt → presentAt.
#      "If X is constant part of something that is present at Y then X is
#       present at Y."
add_chain(presentAt, [constantPartOf, presentAt])

# E-7. constantParticipantOf ∘ presentAt → presentAt.
#      "If X is constant participant of something that is present at Y
#       then X is present at Y."
add_chain(presentAt, [constantParticipantOf, presentAt])

# E-8. constantProperPartOf ∘ presentAt → presentAt.
#      "If X is constant proper part of something that is present at Y
#       then X is present at Y."
add_chain(presentAt, [constantProperPartOf, presentAt])

# E-9. directQualityOf ∘ presentAt → presentAt.
#      "If X is a direct quality of something that is present at Y then
#       X is present at Y." [Dd28, Dd32, Dd33, Dd34, Dd40]
add_chain(presentAt, [directQualityOf, presentAt])

# E-10. presentAt ∘ Inverse(partOf) → presentAt.
#       "If X is present at something that has Y as part then X is
#        present at Y." [Td17]
add_chain(presentAt, [presentAt, Inverse(partOf, simplify=False)])

# E-11. Inverse(directQualityOf) ∘ presentAt → presentAt.
#       "If X has something that is present at Y as direct quality then
#        X is present at Y." [Dd28, Dd32, Dd33, Dd34, Dd40]
add_chain(presentAt, [Inverse(directQualityOf, simplify=False), presentAt])

# E-12. Inverse(partOf) ∘ presentAt → presentAt.
#       "If X has something that is present at Y as part then X is
#        present at Y."
add_chain(presentAt, [Inverse(partOf, simplify=False), presentAt])

# E-13. Inverse(specificallyDependsOn) ∘ presentAt → presentAt.
#       "If X is specifically depended on by something that is present at
#        Y then X is present at Y." [Approximation of Dd69]
add_chain(presentAt, [Inverse(specificallyDependsOn, simplify=False), presentAt])
