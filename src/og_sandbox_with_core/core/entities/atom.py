"""Atom — direct subclass of Particular."""

from og_sandbox_with_core.engine import Or
from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.particular import Particular
from og_sandbox_with_core.core.entities.abstract import Abstract
from og_sandbox_with_core.core.entities.perdurant import Perdurant


with core:

    class Atom(Particular):
        """Atom (atomic Abstract or Perdurant)"""

    # genid203: Atom is_a (Abstract ⊔ Perdurant)
    Atom.is_a.append(Or([Abstract, Perdurant]))

    Atom.label = ["Atom"]


__all__ = ["Atom"]
