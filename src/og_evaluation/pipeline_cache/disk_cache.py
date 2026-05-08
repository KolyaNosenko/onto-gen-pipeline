
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class PipelineArtifacts:

    ttl: str
    main_py: str | None = None


class TtlDiskCache:
    def __init__(
        self,
        root: Path,
        model_id: str,
    ) -> None:
        self._root = Path(root)
        self._root.mkdir(parents=True, exist_ok=True)
        self._model_id = model_id

    def key_for(self, scenario_text: str) -> str:
        h = hashlib.sha256()
        h.update(self._model_id.encode("utf-8"))
        h.update(b"\x00")
        h.update(scenario_text.encode("utf-8"))
        return h.hexdigest()

    def ttl_path_for(self, scenario_text: str) -> Path:
        return self._root / f"{self.key_for(scenario_text)}.ttl"

    def main_py_path_for(self, scenario_text: str) -> Path:
        return self._root / f"{self.key_for(scenario_text)}.main.py"

    # Back-compat alias used by some callers and tests.
    def path_for(self, scenario_text: str) -> Path:
        return self.ttl_path_for(scenario_text)

    def get(self, scenario_text: str) -> PipelineArtifacts | None:
        ttl_path = self.ttl_path_for(scenario_text)
        if not ttl_path.exists():
            return None
        ttl = ttl_path.read_text(encoding="utf-8")
        if not ttl:
            # Empty TTL is treated as a miss so transient failures are retried.
            return None
        main_py_path = self.main_py_path_for(scenario_text)
        main_py = (
            main_py_path.read_text(encoding="utf-8")
            if main_py_path.exists()
            else None
        )
        return PipelineArtifacts(ttl=ttl, main_py=main_py)

    def get_ttl(self, scenario_text: str) -> str | None:
        artifacts = self.get(scenario_text)
        return artifacts.ttl if artifacts is not None else None

    def put(self, scenario_text: str, artifacts: PipelineArtifacts) -> Path:
        ttl_path = self.ttl_path_for(scenario_text)
        ttl_path.write_text(artifacts.ttl, encoding="utf-8")
        if artifacts.main_py is not None:
            self.main_py_path_for(scenario_text).write_text(
                artifacts.main_py, encoding="utf-8"
            )
        return ttl_path

    def get_or_compute(
        self,
        scenario_text: str,
        compute: Callable[[], PipelineArtifacts],
    ) -> PipelineArtifacts:
        cached = self.get(scenario_text)
        if cached is not None:
            return cached
        artifacts = compute()
        if artifacts.ttl:
            self.put(scenario_text, artifacts)
        return artifacts
