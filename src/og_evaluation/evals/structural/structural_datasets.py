
from __future__ import annotations

from pathlib import Path

import pandas as pd
from ragas import Dataset

DEFAULT_DATASET_PATH = (
    Path(__file__).resolve().parents[2]
    / "data" / "docred" / "docred.csv"
)


def get_docred_structural_dataset(
    dataset_path: Path | None = None,
) -> Dataset:
    target = dataset_path or DEFAULT_DATASET_PATH
    df = pd.read_csv(target)
    return Dataset.from_pandas(
        dataframe=df,
        name="structural_docred",
        backend="local/csv",
        root_dir="",
    )
