
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def write_failure_log(
    output_dir: Path,
    row_id: int | str,
    *,
    pipeline_status: str,
    text_snapshot: str | None,
    failure_traceback: str | None,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{row_id}.failure.txt"
    snapshot = (text_snapshot or "")[:500]
    trace = (failure_traceback or "(no traceback — pipeline returned empty TTL)").strip()
    path.write_text(
        "\n".join(
            [
                f"# id: {row_id}",
                f"# timestamp: {datetime.now(tz=timezone.utc).isoformat()}",
                f"# pipeline_status: {pipeline_status}",
                "",
                "## text (first 500 chars)",
                snapshot,
                "",
                "## traceback",
                trace,
                "",
            ]
        ),
        encoding="utf-8",
    )
    return path
