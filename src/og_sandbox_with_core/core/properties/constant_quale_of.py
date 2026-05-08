"""constantQualeOf — ObjectProperty over (AbstractRegion ⊔ PhysicalRegion) → (AbstractQuality ⊔ PhysicalQuality)."""

from og_sandbox_with_core.engine import ObjectProperty, Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.abstract_region import AbstractRegion
from og_sandbox_with_core.core.entities.physical_region import PhysicalRegion
from og_sandbox_with_core.core.entities.abstract_quality import AbstractQuality
from og_sandbox_with_core.core.entities.physical_quality import PhysicalQuality


with core:

    class constantQualeOf(ObjectProperty):
        """
        constantQualeOf is the constant version of Temporary Quale Of
        which is a ternary relation among a physical region x, a
        physical quality y and a time interval t or among an abstract
        region x, an abstract quality y and a time interval t. It
        relates the quality to its quale (position) at a certain
        time.
In this constant version, the region x is the quale of
        the quality y during the whole existence of y.
        """
        domain = [Or([AbstractRegion, PhysicalRegion])]
        range = [Or([AbstractQuality, PhysicalQuality])]

    constantQualeOf.label = ["constant quale of"]


__all__ = ["constantQualeOf"]
