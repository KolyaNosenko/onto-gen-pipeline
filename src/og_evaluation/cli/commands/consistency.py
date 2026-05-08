
from __future__ import annotations

import asyncio
import logging
from typing import Annotated

import typer
from ragas import Dataset

from og_agents.config import AppConfig
from og_evaluation.config import (
    CACHE_ROOT,
    DEFAULT_LANGUAGE_MODEL,
    EXPERIMENTS_ROOT,
)
from og_evaluation.evals.consistency import (
    evaluate_consistency,
    get_docred_consistency_dataset,
)
from og_evaluation.evals.create_experiment_name import (
    create_cache_name,
    create_experiment_name,
)
from og_evaluation.pipeline_cache import TtlDiskCache
from og_evaluation.workflows import DEFAULT_VARIANT, OntologyGenerationWorkflowFactory

app = typer.Typer(no_args_is_help=False)


@app.callback(invoke_without_command=True)
def evaluate_consistency_command(
    language_model_name: Annotated[
        str | None,
        typer.Option("--language-model", "-m"),
    ] = None,
    limit: Annotated[
        int | None,
        typer.Option("--limit"),
    ] = None,
    retry: Annotated[
        int,
        typer.Option(
            "--retry",
            help="Additional pipeline attempts after the first one returns empty TTL.",
        ),
    ] = 0,
    variant: Annotated[
        str,
        typer.Option(
            "--variant",
            help="Workflow pipeline variant (legacy_llm | coding_no_core | coding_with_core).",
        ),
    ] = DEFAULT_VARIANT,
    use_cq: Annotated[
        bool,
        typer.Option(
            "--use-cq/--no-cq",
            help="Insert the GenerateCompetencyQuestions node before the "
                 "ontology stage. Default: enabled.",
        ),
    ] = True,
    logging_level: Annotated[int, typer.Option("--logs", "-l")] = logging.INFO,
):
    logging.basicConfig(level=logging_level)
    asyncio.run(
        _evaluate(
            language_model_name=language_model_name,
            limit=limit,
            retry=retry,
            variant=variant,
            use_cq=use_cq,
        )
    )


async def _evaluate(
    language_model_name: str | None,
    limit: int | None,
    retry: int,
    variant: str,
    use_cq: bool,
) -> None:
    app_config = AppConfig(language_model_name=language_model_name)
    model_name = app_config.language_model_name or DEFAULT_LANGUAGE_MODEL

    dataset = get_docred_consistency_dataset()
    if limit is not None and limit < len(dataset):
        df = dataset.to_pandas().head(limit)
        dataset = Dataset.from_pandas(
            dataframe=df,
            name=f"{dataset.name}.limit{limit}",
            backend="local/csv",
            root_dir="",
        )

    workflow = OntologyGenerationWorkflowFactory.create(
        language_model_name=model_name, variant=variant, use_cq=use_cq
    )

    experiment_name = create_experiment_name(
        base_name="consistency",
        dataset="docred",
        model=model_name,
        use_cq=use_cq,
        variant=variant,
    )
    output_dir = EXPERIMENTS_ROOT / experiment_name
    cache_name = create_cache_name(
        model=model_name, variant=variant, use_cq=use_cq
    )
    cache = TtlDiskCache(
        root=CACHE_ROOT / cache_name,
        model_id=model_name,
    )

    await evaluate_consistency(
        dataset=dataset,
        workflow=workflow,
        cache=cache,
        experiment_name=experiment_name,
        output_dir=output_dir,
        model_id=model_name,
        retry=retry,
    )
