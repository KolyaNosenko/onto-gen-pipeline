"""partOf — transitive ObjectProperty, subPropertyOf overlaps."""

from og_sandbox_with_core.engine import TransitiveProperty, Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.abstract import Abstract
from og_sandbox_with_core.core.entities.perdurant import Perdurant
from og_sandbox_with_core.core.properties.overlaps import overlaps


with core:

    class partOf(overlaps, TransitiveProperty):
        """
        PartOf is a binary relation that is a partial ordering between
        abstract entities or between perdurants. It founds an
        extensional mereology on each of these two categories.
        """
        domain = [Or([Abstract, Perdurant])]
        range = [Or([Abstract, Perdurant])]

    partOf.label = ["part of"]


__all__ = ["partOf"]
