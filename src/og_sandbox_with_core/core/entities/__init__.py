# Entity (OWL Class) declarations.
#
# Each module in this package contributes exactly one OWL Class to the
# core ontology, declared inside its own `with core:` block.
# Imports MUST follow topological order: a class can only be imported after
# all of its parents have been imported, otherwise owlready2 cannot resolve
# the inheritance.

from og_sandbox_with_core.core.entities.particular import Particular  # noqa: F401
from og_sandbox_with_core.core.entities.abstract import Abstract  # noqa: F401
from og_sandbox_with_core.core.entities.endurant import Endurant  # noqa: F401
from og_sandbox_with_core.core.entities.perdurant import Perdurant  # noqa: F401
from og_sandbox_with_core.core.entities.quality import Quality  # noqa: F401
from og_sandbox_with_core.core.entities.atom import Atom  # noqa: F401
from og_sandbox_with_core.core.entities.region import Region  # noqa: F401
from og_sandbox_with_core.core.entities.abstract_region import AbstractRegion  # noqa: F401
from og_sandbox_with_core.core.entities.physical_region import PhysicalRegion  # noqa: F401
from og_sandbox_with_core.core.entities.temporal_region import TemporalRegion  # noqa: F401
from og_sandbox_with_core.core.entities.time_interval import TimeInterval  # noqa: F401
from og_sandbox_with_core.core.entities.abstract_quality import AbstractQuality  # noqa: F401
from og_sandbox_with_core.core.entities.physical_quality import PhysicalQuality  # noqa: F401
from og_sandbox_with_core.core.entities.temporal_quality import TemporalQuality  # noqa: F401
from og_sandbox_with_core.core.entities.arbitrary_sum import ArbitrarySum  # noqa: F401
from og_sandbox_with_core.core.entities.non_physical_endurant import (  # noqa: F401
    NonPhysicalEndurant,
)
from og_sandbox_with_core.core.entities.physical_endurant import PhysicalEndurant  # noqa: F401
from og_sandbox_with_core.core.entities.constant_atom import ConstantAtom  # noqa: F401
from og_sandbox_with_core.core.entities.spatial_location import SpatialLocation  # noqa: F401
from og_sandbox_with_core.core.entities.temporal_location import TemporalLocation  # noqa: F401
from og_sandbox_with_core.core.entities.event import Event  # noqa: F401
from og_sandbox_with_core.core.entities.stative import Stative  # noqa: F401
from og_sandbox_with_core.core.entities.accomplishment import Accomplishment  # noqa: F401
from og_sandbox_with_core.core.entities.achievement import Achievement  # noqa: F401
from og_sandbox_with_core.core.entities.process import Process  # noqa: F401
from og_sandbox_with_core.core.entities.state import State  # noqa: F401
from og_sandbox_with_core.core.entities.physical_object import PhysicalObject  # noqa: F401
from og_sandbox_with_core.core.entities.agentive_physical_object import (  # noqa: F401
    AgentivePhysicalObject,
)
from og_sandbox_with_core.core.entities.non_agentive_physical_object import (  # noqa: F401
    NonAgentivePhysicalObject,
)
from og_sandbox_with_core.core.entities.amount_of_matter import AmountOfMatter  # noqa: F401
from og_sandbox_with_core.core.entities.feature import Feature  # noqa: F401
from og_sandbox_with_core.core.entities.non_physical_object import NonPhysicalObject  # noqa: F401
from og_sandbox_with_core.core.entities.mental_object import MentalObject  # noqa: F401
from og_sandbox_with_core.core.entities.social_object import SocialObject  # noqa: F401
from og_sandbox_with_core.core.entities.agentive_social_object import (  # noqa: F401
    AgentiveSocialObject,
)
from og_sandbox_with_core.core.entities.non_agentive_social_object import (  # noqa: F401
    NonAgentiveSocialObject,
)
from og_sandbox_with_core.core.entities.social_agent import SocialAgent  # noqa: F401
from og_sandbox_with_core.core.entities.society import Society  # noqa: F401
from og_sandbox_with_core.core.entities.space_region import SpaceRegion  # noqa: F401

__all__ = [
    "Particular",
    "Abstract",
    "Endurant",
    "Perdurant",
    "Quality",
    "Atom",
    "Region",
    "AbstractRegion",
    "PhysicalRegion",
    "TemporalRegion",
    "TimeInterval",
    "AbstractQuality",
    "PhysicalQuality",
    "TemporalQuality",
    "ArbitrarySum",
    "NonPhysicalEndurant",
    "PhysicalEndurant",
    "ConstantAtom",
    "SpatialLocation",
    "TemporalLocation",
    "Event",
    "Stative",
    "Accomplishment",
    "Achievement",
    "Process",
    "State",
    "PhysicalObject",
    "AgentivePhysicalObject",
    "NonAgentivePhysicalObject",
    "AmountOfMatter",
    "Feature",
    "NonPhysicalObject",
    "MentalObject",
    "SocialObject",
    "AgentiveSocialObject",
    "NonAgentiveSocialObject",
    "SocialAgent",
    "Society",
    "SpaceRegion",
]
