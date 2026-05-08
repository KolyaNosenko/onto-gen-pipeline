
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class OracleRecallResult:
    matched: int
    total: int
    matched_labels: list[str]

    @property
    def recall(self) -> float:
        return self.matched / self.total if self.total else 0.0


def _label_pattern(label: str) -> re.Pattern[str]:
    tokens = label.strip().split()
    if not tokens:
        return re.compile(r"$^")
    pattern = r"\b" + r"\s+".join(re.escape(t) for t in tokens) + r"\b"
    return re.compile(pattern, flags=re.IGNORECASE)


def _matches_any_variant(text: str, variants: list[str]) -> bool:
    for variant in variants:
        if not variant.strip():
            continue
        if _label_pattern(variant).search(text):
            return True
    return False


def compute_oracle_recall_with_variants(
    text: str, gold_match_sets: list[list[str]], canonical_labels: list[str]
) -> OracleRecallResult:
    if not gold_match_sets:
        return OracleRecallResult(matched=0, total=0, matched_labels=[])
    if len(canonical_labels) != len(gold_match_sets):
        raise ValueError(
            "canonical_labels and gold_match_sets must be the same length"
        )

    matched_canonical: list[str] = []
    seen: set[str] = set()
    for canonical, variants in zip(canonical_labels, gold_match_sets):
        key = canonical.casefold()
        if key in seen:
            continue
        seen.add(key)
        if _matches_any_variant(text, variants):
            matched_canonical.append(canonical)
    return OracleRecallResult(
        matched=len(matched_canonical),
        total=len(seen),
        matched_labels=matched_canonical,
    )


def compute_oracle_recall(
    text: str, gold_labels: list[str]
) -> OracleRecallResult:
    return compute_oracle_recall_with_variants(
        text=text,
        gold_match_sets=[[label] for label in gold_labels],
        canonical_labels=gold_labels,
    )
