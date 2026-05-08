from __future__ import annotations

import re

_FENCE_RE = re.compile(
    r"\A\s*```[A-Za-z0-9_-]*\s*\n(?P<body>.*?)\n```\s*\Z",
    re.DOTALL,
)


def strip_markdown_fence(text: str) -> str:
    if not text:
        return text
    match = _FENCE_RE.match(text)
    if match is None:
        return text
    return match.group("body")
