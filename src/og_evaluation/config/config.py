
from __future__ import annotations

from pathlib import Path

DEFAULT_LANGUAGE_MODEL = "claude-sonnet-4-6"

REPO_ROOT = Path(__file__).resolve().parents[3]

EXPERIMENTS_ROOT = REPO_ROOT / "experiments"

CACHE_ROOT = REPO_ROOT / ".cache" / "og-evaluation"
