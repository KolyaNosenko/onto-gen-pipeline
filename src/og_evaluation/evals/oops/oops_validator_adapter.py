
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Literal

from og_agents.common.http_client import RequestsHttpClient
from og_agents.config import AppConfig
from og_agents.ontology.validators.oops import OOPSOntologyValidator
from og_agents.ontology.validators.oops.oops_pitfall import OOPSPitfall

logger = logging.getLogger(__name__)


OOPSOutcome = Literal[
    "no_pitfalls",
    "has_pitfalls",
    "empty_ttl",
    "validator_error",
]

CriticalityTier = Literal["clean", "minor_only", "important", "critical"]

_IMPORTANCE_WEIGHT: dict[str, int] = {
    "critical": 3,
    "important": 2,
    "minor": 1,
}


def _normalize_importance(raw: str | None) -> str:
    return (raw or "").strip().lower()


@dataclass
class OOPSCheckResult:
    outcome: OOPSOutcome
    pitfalls: list[OOPSPitfall] = field(default_factory=list)
    error: str | None = None

    @property
    def total_pitfalls(self) -> int:
        return len(self.pitfalls)

    def count_by_importance(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for pitfall in self.pitfalls:
            counts[pitfall.importance] = counts.get(pitfall.importance, 0) + 1
        return counts

    def count_by_code(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for pitfall in self.pitfalls:
            counts[pitfall.code] = counts.get(pitfall.code, 0) + 1
        return counts

    def total_affected_elements(self) -> int:
        return sum(p.number_affected or 0 for p in self.pitfalls)

    def n_critical(self) -> int:
        return sum(
            1 for p in self.pitfalls
            if _normalize_importance(p.importance) == "critical"
        )

    def n_important(self) -> int:
        return sum(
            1 for p in self.pitfalls
            if _normalize_importance(p.importance) == "important"
        )

    def n_minor(self) -> int:
        return sum(
            1 for p in self.pitfalls
            if _normalize_importance(p.importance) == "minor"
        )

    def criticality_tier(self) -> CriticalityTier:
        if self.n_critical() > 0:
            return "critical"
        if self.n_important() > 0:
            return "important"
        if self.n_minor() > 0:
            return "minor_only"
        return "clean"

    def weighted_pitfall_score(self) -> int:
        return sum(
            _IMPORTANCE_WEIGHT.get(_normalize_importance(p.importance), 0)
            for p in self.pitfalls
        )


def run_oops(prediction_ttl: str) -> OOPSCheckResult:
    if not prediction_ttl or not prediction_ttl.strip():
        return OOPSCheckResult(outcome="empty_ttl", error="empty TTL input")

    try:
        config = AppConfig.init()
        http_client = RequestsHttpClient()
        validator = OOPSOntologyValidator(http_client=http_client, config=config)
        result = validator.validate_ttl(prediction_ttl)
    except Exception as exc:  # pylint: disable=broad-except
        logger.exception("OOPS! validator crashed")
        return OOPSCheckResult(outcome="validator_error", error=repr(exc))

    pitfalls = list(result.pitfalls)
    return OOPSCheckResult(
        outcome="no_pitfalls" if not pitfalls else "has_pitfalls",
        pitfalls=pitfalls,
    )
