import os
from langchain_anthropic import ChatAnthropic
from og_agents.config import AppConfig
from og_agents.language_models.language_model import LanguageModel


class AnthropicLanguageModel(LanguageModel, ChatAnthropic):
    @staticmethod
    def create(config: AppConfig):
        if not config.model_provider_api_key:
            raise ValueError("Model provider API key not found")

        if os.environ.get("ANTHROPIC_API_KEY") is None:
            os.environ["ANTHROPIC_API_KEY"] = config.model_provider_api_key

        params = {
            "model": config.language_model_name,
            "max_tokens": config.language_model_max_tokens,
            # temperature=None,
            # timeout=None,
            # max_retries=2,
            # api_key="...", If you prefer to pass api key in directly
            # base_url="...",
            # other params...
        }

        return ChatAnthropic(**params)
