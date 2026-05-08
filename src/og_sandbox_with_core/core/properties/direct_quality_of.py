"""directQualityOf — Functional ObjectProperty, subPropertyOf specificallyDependsOn."""

from og_sandbox_with_core.engine import FunctionalProperty, Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.endurant import Endurant
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.entities.quality import Quality
from og_sandbox_with_core.core.properties.specifically_depends_on import specificallyDependsOn


with core:

    class directQualityOf(specificallyDependsOn, FunctionalProperty):
        """
        directQualityOf is a binary relation between a quality and the
        unique entity it inheres in, which is an endurant or a
        perdurant. It implies specific constant dependence.
        """
        domain = [Quality]
        range = [Or([Endurant, Perdurant])]

    directQualityOf.label = ["direct quality of"]


__all__ = ["directQualityOf"]
