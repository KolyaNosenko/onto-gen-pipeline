
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

from og_agents.config.database_config import DatabaseConfig

load_dotenv()

DEFAULT_APP_ENV = "dev"
DEFAULT_MODEL_PROVIDER = "anthropic"
DEFAULT_LANGUAGE_MODEL_MAX_TOKENS = 8192
DEFAULT_OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_OOPS_IGNORED_PITFALLS: tuple[str, ...] = ("P08", "P13")
DEFAULT_CODING_AGENT_LOGS_DIR = Path("logs") / "coding_agent"
DEFAULT_ONTOLOGY_NAME = "https://og.example.org/ontology"


class AppConfig:
    app_env: str
    model_provider: str
    model_provider_api_key: str | None
    language_model_name: str | None
    language_model_max_tokens: int
    openrouter_base_url: str
    openrouter_referer: str | None
    openrouter_title: str | None
    embeddings_model_name: str | None
    oops_api_url: str | None
    oops_ignored_pitfalls: tuple[str, ...]
    ontology_name: str | None
    coding_agent_logs_dir: Path | None
    db: DatabaseConfig

    def __init__(
        self,
        *,
        app_env: str | None = None,
        model_provider: str | None = None,
        model_provider_api_key: str | None = None,
        language_model_name: str | None = None,
        language_model_max_tokens: int | None = None,
        openrouter_base_url: str | None = None,
        openrouter_referer: str | None = None,
        openrouter_title: str | None = None,
        embeddings_model_name: str | None = None,
        oops_api_url: str | None = None,
        oops_ignored_pitfalls: tuple[str, ...] | None = None,
        ontology_name: str | None = None,
        coding_agent_logs_dir: Path | str | None = None,
        db: DatabaseConfig | None = None,
    ):
        self.app_env = self._resolve(
            app_env, os.getenv("APP_ENV"), DEFAULT_APP_ENV
        )
        self.model_provider = self._resolve(
            model_provider,
            os.getenv("MODEL_PROVIDER"),
            DEFAULT_MODEL_PROVIDER,
        ).lower()
        self.model_provider_api_key = self._resolve(
            model_provider_api_key,
            os.getenv("MODEL_PROVIDER_API_KEY"),
        )
        self.language_model_name = self._resolve(
            language_model_name,
            os.getenv("LANGUAGE_MODEL_NAME"),
        )
        self.language_model_max_tokens = int(
            self._resolve(
                language_model_max_tokens,
                os.getenv("LANGUAGE_MODEL_MAX_TOKENS"),
                DEFAULT_LANGUAGE_MODEL_MAX_TOKENS,
            )
        )
        self.openrouter_base_url = self._resolve(
            openrouter_base_url,
            os.getenv("OPENROUTER_BASE_URL"),
            DEFAULT_OPENROUTER_BASE_URL,
        )
        self.openrouter_referer = self._resolve(
            openrouter_referer,
            os.getenv("OPENROUTER_REFERER"),
        )
        self.openrouter_title = self._resolve(
            openrouter_title,
            os.getenv("OPENROUTER_TITLE"),
        )
        self.embeddings_model_name = self._resolve(
            embeddings_model_name,
            os.getenv("EMBEDDINGS_MODEL_NAME"),
        )
        self.oops_api_url = self._resolve(
            oops_api_url,
            os.getenv("OOPS_API_URL"),
        )
        self.oops_ignored_pitfalls = self._resolve(
            oops_ignored_pitfalls,
            DEFAULT_OOPS_IGNORED_PITFALLS,
        )
        self.ontology_name = self._resolve(
            ontology_name,
            os.getenv("ONTOLOGY_NAME"),
            DEFAULT_ONTOLOGY_NAME,
        )
        logs_dir_raw = self._resolve(
            coding_agent_logs_dir,
            os.getenv("CODING_AGENT_LOGS_DIR"),
            DEFAULT_CODING_AGENT_LOGS_DIR,
        )
        self.coding_agent_logs_dir = (
            Path(logs_dir_raw) if logs_dir_raw is not None else None
        )
        self.db = db or DatabaseConfig()

    @staticmethod
    def _resolve(*values):
        for value in values:
            if value is None:
                continue
            if isinstance(value, str) and value == "":
                continue
            return value
        return None

    @staticmethod
    def init(**overrides) -> "AppConfig":
        return AppConfig(**overrides)
