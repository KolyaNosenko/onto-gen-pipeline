# ObjectProperty declarations.
#
# Each module in this package contributes exactly one OWL ObjectProperty to
# the core ontology, declared inside its own `with core:`
# block. Topological order matters when a property declares another as
# `subPropertyOf` or `inverse_property` — declare the referenced property
# first.

from og_sandbox_with_core.core.properties.overlaps import overlaps  # noqa: F401
from og_sandbox_with_core.core.properties.part_of import partOf  # noqa: F401
from og_sandbox_with_core.core.properties.proper_part_of import properPartOf  # noqa: F401
from og_sandbox_with_core.core.properties.atomic_part_of import atomicPartOf  # noqa: F401
from og_sandbox_with_core.core.properties.present_at import presentAt  # noqa: F401
from og_sandbox_with_core.core.properties.temporally_located_at import (  # noqa: F401
    temporallyLocatedAt,
)
from og_sandbox_with_core.core.properties.specifically_depends_on import (  # noqa: F401
    specificallyDependsOn,
)
from og_sandbox_with_core.core.properties.direct_quality_of import (  # noqa: F401
    directQualityOf,
)
from og_sandbox_with_core.core.properties.constantly_overlaps import (  # noqa: F401
    constantlyOverlaps,
)
from og_sandbox_with_core.core.properties.constant_part_of import (  # noqa: F401
    constantPartOf,
)
from og_sandbox_with_core.core.properties.constant_proper_part_of import (  # noqa: F401
    constantProperPartOf,
)
from og_sandbox_with_core.core.properties.constant_constituent_of import (  # noqa: F401
    constantConstituentOf,
)
from og_sandbox_with_core.core.properties.constant_participant_of import (  # noqa: F401
    constantParticipantOf,
)
from og_sandbox_with_core.core.properties.constant_atomic_part_of import (  # noqa: F401
    constantAtomicPartOf,
)
from og_sandbox_with_core.core.properties.quale_of import qualeOf  # noqa: F401
from og_sandbox_with_core.core.properties.constant_quale_of import (  # noqa: F401
    constantQualeOf,
)
from og_sandbox_with_core.core.properties.temporal_part_of import (  # noqa: F401
    temporalPartOf,
)

__all__ = [
    "overlaps",
    "partOf",
    "properPartOf",
    "atomicPartOf",
    "presentAt",
    "temporallyLocatedAt",
    "specificallyDependsOn",
    "directQualityOf",
    "constantlyOverlaps",
    "constantPartOf",
    "constantProperPartOf",
    "constantConstituentOf",
    "constantParticipantOf",
    "constantAtomicPartOf",
    "qualeOf",
    "constantQualeOf",
    "temporalPartOf",
]
