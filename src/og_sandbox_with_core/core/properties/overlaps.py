"""overlaps — symmetric ObjectProperty over Abstract ⊔ Perdurant."""

from og_sandbox_with_core.engine import ObjectProperty, SymmetricProperty, Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.abstract import Abstract
from og_sandbox_with_core.core.entities.perdurant import Perdurant


with core:

    class overlaps(ObjectProperty, SymmetricProperty):
        """
        overlaps holds between two abstracts or two perdurants when they
        both share a part.
        """
        domain = [Or([Abstract, Perdurant])]
        range = [Or([Abstract, Perdurant])]

    overlaps.label = ["overlaps"]


__all__ = ["overlaps"]
