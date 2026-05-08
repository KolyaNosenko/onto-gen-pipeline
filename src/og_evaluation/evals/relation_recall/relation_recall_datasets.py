
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from ragas import Dataset

DEFAULT_DATASET_PATH = (
    Path(__file__).resolve().parents[2]
    / "data" / "docred" / "docred.csv"
)


def get_docred_relation_recall_dataset(
    dataset_path: Path | None = None,
) -> Dataset:
    target = dataset_path or DEFAULT_DATASET_PATH
    df = pd.read_csv(target)

    head_mentions: list[str] = []
    tail_mentions: list[str] = []
    for _, row in df.iterrows():
        em = json.loads(row["entity_mentions"])
        head_idx = json.loads(row["head_indices"])
        tail_idx = json.loads(row["tail_indices"])
        head_mentions.append(json.dumps([em[i] for i in head_idx]))
        tail_mentions.append(json.dumps([em[i] for i in tail_idx]))
    df = df.copy()
    df["head_mentions"] = head_mentions
    df["tail_mentions"] = tail_mentions

    return Dataset.from_pandas(
        dataframe=df,
        name="relation_recall_docred",
        backend="local/csv",
        root_dir="",
    )
