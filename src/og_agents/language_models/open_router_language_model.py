import os
from langchain_openai import ChatOpenAI
from og_agents.config import AppConfig
from og_agents.language_models.language_model import LanguageModel


class OpenRouterLanguageModel(LanguageModel, ChatOpenAI):
    @staticmethod
    def create(config: AppConfig):
        if not config.model_provider_api_key:
            raise ValueError("Model provider API key not found")

        if os.environ.get("OPENROUTER_API_KEY") is None:
            os.environ["OPENROUTER_API_KEY"] = config.model_provider_api_key

        default_headers: dict[str, str] = {}
        if config.openrouter_referer:
            default_headers["HTTP-Referer"] = config.openrouter_referer
        if config.openrouter_title:
            default_headers["X-Title"] = config.openrouter_title

        params = {
            "model": config.language_model_name,
            "base_url": config.openrouter_base_url,
            "api_key": config.model_provider_api_key,
            "max_tokens": config.language_model_max_tokens,
        }
        if default_headers:
            params["default_headers"] = default_headers

        return ChatOpenAI(**params)
