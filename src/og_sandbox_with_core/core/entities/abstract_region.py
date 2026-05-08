"""AbstractRegion — direct subclass of Region."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.region import Region


with core:

    class AbstractRegion(Region):
        """
        An Abstract Region is a region in the abstract quality space for
        abstract qualities (example: the conventional value of 1 Euro).
        """

    AbstractRegion.label = ["Abstract Region"]


__all__ = ["AbstractRegion"]
