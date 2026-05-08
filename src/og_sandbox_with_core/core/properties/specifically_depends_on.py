"""specificallyDependsOn — Transitive ObjectProperty over (Endurant ⊔ Perdurant ⊔ Quality)."""

from og_sandbox_with_core.engine import ObjectProperty, TransitiveProperty, Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.entities.quality import Quality


with core:

    class specificallyDependsOn(ObjectProperty, TransitiveProperty):
        """
        Specific Constant DependencespecificallyDependsOn is a binary
        relation between two entities x, y present in time, i.e.,
        endurants, perdurants or qualities, with the intended
        interpretation that the existence of x specifically and
        constantly depends on the existence of y.
        """
        domain = [Or([Endurant, Perdurant, Quality])]
        range = [Or([Endurant, Perdurant, Quality])]

    specificallyDependsOn.label = ["specifically depends on"]


__all__ = ["specificallyDependsOn"]
