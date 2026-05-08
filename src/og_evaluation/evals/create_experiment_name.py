
from __future__ import annotations

import re


_UNSAFE = re.compile(r"[^A-Za-z0-9._-]+")


def _sanitize(value: object) -> str:
    return _UNSAFE.sub("-", str(value)).strip("-") or "x"


def create_experiment_name(base_name: str, **kwargs: object) -> str:
    parts = [_sanitize(base_name)]
    for key in sorted(kwargs):
        value = kwargs[key]
        if value is None:
            continue
        parts.append(f"{_sanitize(key)}={_sanitize(value)}")
    return ".".join(parts)


def create_cache_name(*, model: str, variant: str, use_cq: bool) -> str:
    return create_experiment_name(
        "pipeline", model=model, use_cq=use_cq, variant=variant
    )
