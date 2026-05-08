from og_sandbox_with_core.core.ontology import NS_IRI, core

# Submodules are imported for their side effect of declaring entities and
# properties on `core`. Topological order is enforced inside each
# subpackage's __init__.
from og_sandbox_with_core.core import entities  # noqa: F401
from og_sandbox_with_core.core import properties  # noqa: F401

# Cross-entity axioms run AFTER all entities and properties so every name
# they reference is already on `core`.
from og_sandbox_with_core.core import axioms  # noqa: F401

# Property chains run last because they reference many properties.
from og_sandbox_with_core.core import property_chains  # noqa: F401

__all__ = [
    "NS_IRI",
    "core",
]
