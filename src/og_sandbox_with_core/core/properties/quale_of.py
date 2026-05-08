"""qualeOf — InverseFunctionalProperty, domain TemporalRegion, range TemporalQuality."""

from og_sandbox_with_core.engine import ObjectProperty, InverseFunctionalProperty
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.temporal_region import TemporalRegion
from og_sandbox_with_core.core.entities.temporal_quality import TemporalQuality


with core:

    class qualeOf(ObjectProperty, InverseFunctionalProperty):
        """
        aka immediate qualequaleOf is a binary relation between a
        temporal region and a temporal quality, relating the quality to
        its quale (position in the quality space).
        """
        domain = [TemporalRegion]
        range = [TemporalQuality]

    qualeOf.label = ["quale of"]


__all__ = ["qualeOf"]
