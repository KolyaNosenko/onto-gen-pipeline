
from __future__ import annotations

import contextlib
import logging
import os
import tempfile
import time
from dataclasses import dataclass, field
from typing import Literal

logger = logging.getLogger(__name__)

ReasonerOutcome = Literal[
    "consistent",
    "incoherent",
    "inconsistent",
    "parse_error",
    "reasoner_error",
    "empty_ttl",
]


@dataclass
class ReasonerResult:
    outcome: ReasonerOutcome
    is_consistent: bool
    n_classes: int = 0
    n_individuals: int = 0
    n_unsatisfiable: int = 0
    unsatisfiable_iris: list[str] = field(default_factory=list)
    reasoning_time_s: float = 0.0
    error: str | None = None

    @property
    def is_clean(self) -> bool:
        return self.outcome == "consistent"


def check_consistency(prediction_ttl: str) -> ReasonerResult:
    if not prediction_ttl or not prediction_ttl.strip():
        return ReasonerResult(
            outcome="empty_ttl",
            is_consistent=False,
            error="empty TTL input",
        )

    try:
        import owlready2  # local import — heavy module
    except ImportError as exc:  # pragma: no cover
        return ReasonerResult(
            outcome="reasoner_error",
            is_consistent=False,
            error=f"owlready2 unavailable: {exc!r}",
        )

    # owlready2 only loads RDF/XML, OWL/XML, or NTriples. We re-serialise
    # the Turtle into RDF/XML via rdflib first.
    try:
        import rdflib

        graph = rdflib.Graph()
        graph.parse(data=prediction_ttl, format="turtle")
        rdfxml = graph.serialize(format="xml")
    except Exception as exc:  # pylint: disable=broad-except
        return ReasonerResult(
            outcome="parse_error",
            is_consistent=False,
            error=f"turtle→rdf/xml conversion failed: {exc!r}",
        )

    with tempfile.NamedTemporaryFile(
        suffix=".owl", mode="w", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(rdfxml if isinstance(rdfxml, str) else rdfxml.decode("utf-8"))
        tmp_path = tmp.name

    try:
        world = owlready2.World()
        try:
            ontology = world.get_ontology(f"file://{tmp_path}").load()
        except Exception as exc:  # pylint: disable=broad-except
            return ReasonerResult(
                outcome="parse_error",
                is_consistent=False,
                error=f"owlready2 load failed: {exc!r}",
            )

        n_classes = len(list(ontology.classes()))
        n_individuals = len(list(ontology.individuals()))

        started = time.perf_counter()
        try:
            with ontology:
                owlready2.sync_reasoner_pellet(world)
        except owlready2.OwlReadyInconsistentOntologyError as exc:
            return ReasonerResult(
                outcome="inconsistent",
                is_consistent=False,
                n_classes=n_classes,
                n_individuals=n_individuals,
                reasoning_time_s=time.perf_counter() - started,
                error=str(exc),
            )
        except Exception as exc:  # pylint: disable=broad-except
            logger.exception("reasoner crashed on Turtle of length %d", len(prediction_ttl))
            return ReasonerResult(
                outcome="reasoner_error",
                is_consistent=False,
                n_classes=n_classes,
                n_individuals=n_individuals,
                reasoning_time_s=time.perf_counter() - started,
                error=repr(exc),
            )
        elapsed = time.perf_counter() - started

        unsatisfiable = list(world.inconsistent_classes())
        unsat_iris = [getattr(cls, "iri", str(cls)) for cls in unsatisfiable]

        if unsat_iris:
            return ReasonerResult(
                outcome="incoherent",
                is_consistent=True,
                n_classes=n_classes,
                n_individuals=n_individuals,
                n_unsatisfiable=len(unsat_iris),
                unsatisfiable_iris=unsat_iris,
                reasoning_time_s=elapsed,
            )
        return ReasonerResult(
            outcome="consistent",
            is_consistent=True,
            n_classes=n_classes,
            n_individuals=n_individuals,
            reasoning_time_s=elapsed,
        )
    finally:
        with contextlib.suppress(OSError):
            os.unlink(tmp_path)
