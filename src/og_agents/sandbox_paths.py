from pathlib import Path

_SRC_DIR = Path(__file__).resolve().parent.parent

WITH_CORE_ENV_DIR: Path = _SRC_DIR / "og_sandbox_with_core"
NO_CORE_ENV_DIR: Path = _SRC_DIR / "og_sandbox_no_core"

__all__ = ["WITH_CORE_ENV_DIR", "NO_CORE_ENV_DIR"]
