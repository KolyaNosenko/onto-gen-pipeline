"""presentAt — ObjectProperty over (Endurant ⊔ Perdurant ⊔ Quality) → TimeInterval."""

from og_sandbox_with_core.engine import ObjectProperty, Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.entities.quality import Quality
from og_sandbox_with_core.core.entities.time_interval import TimeInterval


with core:

    class presentAt(ObjectProperty):
        """
        presentAt is a binary relation between an endurant or a
        perdurant or a quality x and a time interval t which is part of
        x's temporal location.
        """
        domain = [Or([Endurant, Perdurant, Quality])]
        range = [TimeInterval]

    presentAt.label = ["present at"]


__all__ = ["presentAt"]
