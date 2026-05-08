"""Cross-entity axioms — declarations that reference more than one entity."""

from og_sandbox_with_core.engine import AllDisjoint, Inverse, Not
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities import Particular, Abstract, Endurant, Perdurant, Quality
from og_sandbox_with_core.core.entities.atom import Atom
from og_sandbox_with_core.core.entities.region import Region
from og_sandbox_with_core.core.entities.abstract_region import AbstractRegion
from og_sandbox_with_core.core.entities.physical_region import PhysicalRegion
from og_sandbox_with_core.core.entities.temporal_region import TemporalRegion
from og_sandbox_with_core.core.entities.time_interval import TimeInterval
from og_sandbox_with_core.core.entities.abstract_quality import AbstractQuality
from og_sandbox_with_core.core.entities.physical_quality import PhysicalQuality
from og_sandbox_with_core.core.entities.temporal_quality import TemporalQuality
from og_sandbox_with_core.core.entities.arbitrary_sum import ArbitrarySum
from og_sandbox_with_core.core.entities.non_physical_endurant import NonPhysicalEndurant
from og_sandbox_with_core.core.entities.physical_endurant import PhysicalEndurant
from og_sandbox_with_core.core.properties.overlaps import overlaps
from og_sandbox_with_core.core.properties.part_of import partOf
from og_sandbox_with_core.core.properties.proper_part_of import properPartOf
from og_sandbox_with_core.core.properties.temporally_located_at import temporallyLocatedAt
from og_sandbox_with_core.core.properties.direct_quality_of import directQualityOf
from og_sandbox_with_core.core.properties.constantly_overlaps import constantlyOverlaps
from og_sandbox_with_core.core.properties.constant_part_of import constantPartOf
from og_sandbox_with_core.core.properties.constant_proper_part_of import constantProperPartOf
from og_sandbox_with_core.core.properties.constant_constituent_of import constantConstituentOf
from og_sandbox_with_core.core.entities.constant_atom import ConstantAtom
from og_sandbox_with_core.core.entities.spatial_location import SpatialLocation
from og_sandbox_with_core.core.entities.temporal_location import TemporalLocation
from og_sandbox_with_core.core.properties.quale_of import qualeOf
from og_sandbox_with_core.core.properties.constant_quale_of import constantQualeOf
from og_sandbox_with_core.core.entities.event import Event
from og_sandbox_with_core.core.entities.stative import Stative
from og_sandbox_with_core.core.entities.accomplishment import Accomplishment
from og_sandbox_with_core.core.entities.achievement import Achievement
from og_sandbox_with_core.core.entities.process import Process
from og_sandbox_with_core.core.entities.state import State
from og_sandbox_with_core.core.entities.physical_object import PhysicalObject
from og_sandbox_with_core.core.entities.agentive_physical_object import AgentivePhysicalObject
from og_sandbox_with_core.core.entities.non_agentive_physical_object import (
    NonAgentivePhysicalObject,
)
from og_sandbox_with_core.core.entities.amount_of_matter import AmountOfMatter
from og_sandbox_with_core.core.entities.feature import Feature
from og_sandbox_with_core.core.entities.mental_object import MentalObject
from og_sandbox_with_core.core.entities.social_object import SocialObject
from og_sandbox_with_core.core.entities.agentive_social_object import AgentiveSocialObject
from og_sandbox_with_core.core.entities.non_agentive_social_object import (
    NonAgentiveSocialObject,
)
from og_sandbox_with_core.core.entities.social_agent import SocialAgent
from og_sandbox_with_core.core.entities.society import Society
from og_sandbox_with_core.core.entities.space_region import SpaceRegion
from og_sandbox_with_core.core.properties.specifically_depends_on import (  # noqa: F811
    specificallyDependsOn,
)
from og_sandbox_with_core.core.properties.temporally_located_at import temporallyLocatedAt as _tla  # noqa: F401  (already imported above as alias)


with core:
    # A particular is either an abstract, an endurant, a perdurant, or a
    # quality, and the classes Abstract, Endurant, Perdurant and Quality are
    # all disjoint.
    Particular.disjoint_unions.append([Abstract, Endurant, Perdurant, Quality])

    # Everything that overlaps an abstract is an abstract.
    Abstract.is_a.append(overlaps.only(Abstract))

    # Everything that has an abstract as part is an abstract.
    Abstract.is_a.append(partOf.only(Abstract))

    # Everything that is part of an abstract is an abstract
    Abstract.is_a.append(Inverse(partOf).only(Abstract))

    # No atom has a particular as proper part.
    Atom.is_a.append(Not(Inverse(properPartOf).some(Particular)))

    # The classes Region, AbstractRegion, TemporalRegion all disjoint.
    Region.disjoint_unions.append([AbstractRegion, PhysicalRegion, TemporalRegion])

    # Everything that is part of a time interval is a time interval.
    TimeInterval.is_a.append(Inverse(partOf).only(TimeInterval))

    # Every endurant is temporally located at a time interval.
    Endurant.is_a.append(temporallyLocatedAt.some(TimeInterval))

    # Every perdurant is temporally located at a time interval.
    Perdurant.is_a.append(temporallyLocatedAt.some(TimeInterval))

    # Every quality is temporally located at a timeinterval.
    Quality.is_a.append(temporallyLocatedAt.some(TimeInterval))

    # Every quality is direct quality of a particular.
    Quality.is_a.append(directQualityOf.some(Particular))

    # A quality is either an abstract quality, a physical quality, or a
    # temporal quality, and the classes AbstractQuality, PhysicalQuality,
    # and TemporalQuality are all disjoint.
    Quality.disjoint_unions.append([AbstractQuality, PhysicalQuality, TemporalQuality])

    # Every temporal quality is a direct quality of a perdurant.
    TemporalQuality.is_a.append(directQualityOf.only(Perdurant))

    # An endurant is either an arbitrary sum, a physical endurant or a
    # non-physical endurant, and the classes ArbitrarySum, PhysicalEndurant
    # and NonPhysicalEndurant are all disjoint.
    Endurant.disjoint_unions.append([ArbitrarySum, NonPhysicalEndurant, PhysicalEndurant])

    # Everything that is direct quality of a non physical endurant is an abstract quality.
    NonPhysicalEndurant.is_a.append(Inverse(directQualityOf).only(AbstractQuality))

    # Everything that is direct quality of a physical endurant is a physical quality.
    PhysicalEndurant.is_a.append(Inverse(directQualityOf).only(PhysicalQuality))

    # Everything that has an abstract quality as direct quality is a non physical endurant.
    AbstractQuality.is_a.append(directQualityOf.only(NonPhysicalEndurant))

    # Every physical quality is a direct quality of a physical endurant.
    PhysicalQuality.is_a.append(directQualityOf.only(PhysicalEndurant))

    # The defining property of a non-physical endurant: it shares no constant part with any physical endurant.
    NonPhysicalEndurant.is_a.append(
        Not(constantlyOverlaps.some(PhysicalEndurant))
    )

    # Everything that is constant part of a non physical endurant is a non physical endurant.
    NonPhysicalEndurant.is_a.append(
        Inverse(constantPartOf).only(NonPhysicalEndurant)
    )

    # Everything that is constant part of a physical endurant is a physical endurant.
    PhysicalEndurant.is_a.append(Inverse(constantPartOf).only(PhysicalEndurant))

    # NonPhysicalEndurant ⊑ constantConstituentOf only NonPhysicalEndurant.
    NonPhysicalEndurant.is_a.append(
        constantConstituentOf.only(NonPhysicalEndurant)
    )

    # NonPhysicalEndurant ⊑ inverse(constantConstituentOf) only NonPhysicalEndurant.
    NonPhysicalEndurant.is_a.append(
        Inverse(constantConstituentOf).only(NonPhysicalEndurant)
    )

    # PhysicalEndurant ⊑ constantConstituentOf only PhysicalEndurant.
    PhysicalEndurant.is_a.append(constantConstituentOf.only(PhysicalEndurant))

    # PhysicalEndurant ⊑ inverse(constantConstituentOf) only PhysicalEndurant.
    PhysicalEndurant.is_a.append(
        Inverse(constantConstituentOf).only(PhysicalEndurant)
    )

    # ConstantAtom is mereologically atomic w.r.t. constant parthood: no Particular has a ConstantAtom as constant proper part.
    ConstantAtom.is_a.append(
        Not(Inverse(constantProperPartOf).some(Particular))
    )

    # Perdurant ⊑ overlaps only Perdurant.
    Perdurant.is_a.append(overlaps.only(Perdurant))

    # Everything that has a perdurant as part is a perdurant.
    Perdurant.is_a.append(partOf.only(Perdurant))

    # Everything that is part of a perdurant is a perdurant.
    Perdurant.is_a.append(Inverse(partOf).only(Perdurant))

    # Everything that is constantly constituted by a perdurant is a perdurant.
    Perdurant.is_a.append(constantConstituentOf.only(Perdurant))

    # Everything that is constant constituent of a perdurant is a perdurant.
    Perdurant.is_a.append(Inverse(constantConstituentOf).only(Perdurant))

    # Everything that is direct quality of a perdurant is a temporal quality.
    Perdurant.is_a.append(Inverse(directQualityOf).only(TemporalQuality))

    # Every physical endurant has a spatial location as direct quality.
    PhysicalEndurant.is_a.append(
        Inverse(directQualityOf).some(SpatialLocation)
    )

    # Every perdurant has a temporal location as direct quality.
    Perdurant.is_a.append(Inverse(directQualityOf).some(TemporalLocation))

    # Every temporal location has some time interval as quale.
    TemporalLocation.is_a.append(Inverse(qualeOf).some(TimeInterval))

    # Every temporal quality has some particular as quale.
    TemporalQuality.is_a.append(Inverse(qualeOf).some(Particular))

    # Everything that has an abstract region as a constant quale is an abstract quality.
    AbstractRegion.is_a.append(constantQualeOf.only(AbstractQuality))

    # Everything that has an abstract region as part is an abstract region.
    AbstractRegion.is_a.append(partOf.only(AbstractRegion))

    # Everything that is part of an abstract region is an abstract region.
    AbstractRegion.is_a.append(Inverse(partOf).only(AbstractRegion))

    # Everything that has a physical region as constant quale is a physical quality.
    PhysicalRegion.is_a.append(constantQualeOf.only(PhysicalQuality))

    # Everything that is constant quale of an abstract quality is an abstract region.
    AbstractQuality.is_a.append(Inverse(constantQualeOf).only(AbstractRegion))

    # Everything that is constant quale of a physical quality is a physical region.
    PhysicalQuality.is_a.append(Inverse(constantQualeOf).only(PhysicalRegion))

    # Accomplishments are temporally non-atomic.
    Accomplishment.is_a.append(Not(temporallyLocatedAt.some(Atom)))

    # Achievements are temporally atomic.
    Achievement.is_a.append(temporallyLocatedAt.some(Atom))

    # State ⊑ inverse(partOf) only State.
    State.is_a.append(Inverse(partOf).only(State))

    # No event is a stative.
    AllDisjoint([Event, Stative])

    # Accomplishment ↮ Achievement.
    AllDisjoint([Accomplishment, Achievement])

    # No process is a state.
    AllDisjoint([Process, State])

    # PhysicalObject = AgentivePhysicalObject ⊔ NonAgentivePhysicalObject
    PhysicalObject.disjoint_unions.append(
        [AgentivePhysicalObject, NonAgentivePhysicalObject]
    )

    # AmountOfMatter ↮ Feature.
    AllDisjoint([AmountOfMatter, Feature])

    # AmountOfMatter ↮ PhysicalObject.
    AllDisjoint([AmountOfMatter, PhysicalObject])

    # Feature ↮ PhysicalObject.
    AllDisjoint([Feature, PhysicalObject])

    # MentalObject ⊑ specificallyDependsOn some AgentivePhysicalObject.
    MentalObject.is_a.append(
        specificallyDependsOn.some(AgentivePhysicalObject)
    )

    # SocialObject = AgentiveSocialObject ⊔ NonAgentiveSocialObject
    SocialObject.disjoint_unions.append(
        [AgentiveSocialObject, NonAgentiveSocialObject]
    )

    # MentalObject ↮ SocialObject.
    AllDisjoint([MentalObject, SocialObject])

    # SocialAgent ↮ Society.
    AllDisjoint([SocialAgent, Society])

    # SpaceRegion ⊑ constantQualeOf only SpatialLocation.
    SpaceRegion.is_a.append(constantQualeOf.only(SpatialLocation))

    # SpaceRegion ⊑ partOf only SpaceRegion.
    SpaceRegion.is_a.append(partOf.only(SpaceRegion))

    # SpaceRegion ⊑ inverse(partOf) only SpaceRegion.
    SpaceRegion.is_a.append(Inverse(partOf).only(SpaceRegion))
