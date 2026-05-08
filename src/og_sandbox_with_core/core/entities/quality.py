"""Quality — direct subclass of Particular."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.particular import Particular


with core:

    class Quality(Particular):
        """
        A Quality is an entity that inheres in an endurant or a
        perdurant, and that can be perceived or measured (examples: the
        shape of a book, the color of a car, the size of a t-shirt, the
        electrical charge of a battery).
        """

    Quality.label = ["Quality"]


__all__ = ["Quality"]
