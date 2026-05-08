
from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Annotated

import typer

from og_evaluation.config import CACHE_ROOT
from og_evaluation.evals.create_experiment_name import create_cache_name

app = typer.Typer(no_args_is_help=False)

# Mirrors create_experiment_name._sanitize so user-supplied --model /
# --variant values match the directory names on disk.
_UNSAFE = re.compile(r"[^A-Za-z0-9._-]+")


def _sanitize(value: str) -> str:
    return _UNSAFE.sub("-", value).strip("-") or "x"


@app.callback(invoke_without_command=True)
def clear_cache_command(
    model: Annotated[
        str | None,
        typer.Option(
            "--model",
            "-m",
            help="Limit to caches for this language model id.",
        ),
    ] = None,
    variant: Annotated[
        str | None,
        typer.Option(
            "--variant",
            help="Limit to caches for this pipeline variant "
            "(legacy_llm | coding_no_core | coding_with_core).",
        ),
    ] = None,
    yes: Annotated[
        bool,
        typer.Option(
            "--yes",
            "-y",
            help="Skip the confirmation prompt.",
        ),
    ] = False,
):
    if not CACHE_ROOT.exists():
        typer.echo(f"nothing to clear: {CACHE_ROOT} does not exist")
        return

    targets = _select_targets(model=model, variant=variant)
    if not targets:
        typer.echo("nothing to clear (no matching cache directories).")
        return

    typer.echo(f"will delete {len(targets)} cache director{'y' if len(targets) == 1 else 'ies'}:")
    for path in targets:
        typer.echo(f"  {path}")

    if not yes and not typer.confirm("proceed?", default=False):
        typer.echo("aborted.")
        raise typer.Exit(code=1)

    for path in targets:
        shutil.rmtree(path)
        typer.echo(f"removed {path}")


def _select_targets(
    *, model: str | None, variant: str | None
) -> list[Path]:
    candidates = sorted(p for p in CACHE_ROOT.iterdir() if p.is_dir())
    if model is None and variant is None:
        return candidates
    if model is not None and variant is not None:
        # Exact match — single directory.
        target = CACHE_ROOT / create_cache_name(model=model, variant=variant)
        return [target] if target.exists() else []
    # Single-axis filter: match against the relevant `key=value` token.
    needle = (
        f"model={_sanitize(model)}"
        if model is not None
        else f"variant={_sanitize(variant)}"  # type: ignore[arg-type]
    )
    return [p for p in candidates if needle in p.name.split(".")]
