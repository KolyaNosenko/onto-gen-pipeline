"""temporallyLocatedAt — Functional ObjectProperty, subPropertyOf presentAt."""

from og_sandbox_with_core.engine import FunctionalProperty, Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.entities.quality import Quality
from og_sandbox_with_core.core.entities.time_interval import TimeInterval
from og_sandbox_with_core.core.properties.present_at import presentAt


with core:

    class temporallyLocatedAt(presentAt, FunctionalProperty):
        """
        temporallyLocatedAt is a binary relation between an endurant or
        a perdurant or a quality and the unique time interval it is
        exactly located in.
        """
        domain = [Or([Endurant, Perdurant, Quality])]
        range = [TimeInterval]

    temporallyLocatedAt.label = ["temporally located at"]


__all__ = ["temporallyLocatedAt"]
