"""AbstractQuality — direct subclass of Quality."""
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.quality import Quality


with core:

    class AbstractQuality(Quality):
        """
        An Abstract Quality is a quality that directly inheres to a
        non-physical endurant (examples: the value of an asset, the
        rights of the UN general secretary).Warning: Abstract qualities
        are not qualities of abstract entities, but of non-physical
        endurants
        """

    AbstractQuality.label = ["Abstract Quality"]


__all__ = ["AbstractQuality"]
