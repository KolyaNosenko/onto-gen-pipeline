
from __future__ import annotations

import typer

from og_evaluation.cli.commands.clear_cache import (
    app as clear_cache_app,
)
from og_evaluation.cli.commands.consistency import (
    app as consistency_app,
)
from og_evaluation.cli.commands.link_recall import (
    app as link_recall_app,
)
from og_evaluation.cli.commands.oops import (
    app as oops_app,
)
from og_evaluation.cli.commands.relation_recall import (
    app as relation_recall_app,
)
from og_evaluation.cli.commands.structural import (
    app as structural_app,
)
from og_evaluation.cli.commands.term_recall import (
    app as term_recall_app,
)

app = typer.Typer(
    no_args_is_help=True,
    help="Run og_evaluation experiments.",
)
app.add_typer(term_recall_app, name="term-recall")
app.add_typer(link_recall_app, name="link-recall")
app.add_typer(relation_recall_app, name="relation-recall")
app.add_typer(consistency_app, name="consistency")
app.add_typer(oops_app, name="oops")
app.add_typer(structural_app, name="structural")
app.add_typer(clear_cache_app, name="clear-cache")


if __name__ == "__main__":
    app()
