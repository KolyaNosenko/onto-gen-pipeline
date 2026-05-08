from og_agents.config import AppConfig
from og_agents.language_models.language_model import LanguageModel
from og_agents.language_models.open_ai_language_model import OpenAILanguageModel
from og_agents.language_models.anthropic_language_model import AnthropicLanguageModel
from og_agents.language_models.open_router_language_model import OpenRouterLanguageModel
from og_agents.language_models.hugging_face_language_model import HuggingFaceLanguageModel

_PROVIDERS = {
    "anthropic": AnthropicLanguageModel,
    "openai": OpenAILanguageModel,
    "openrouter": OpenRouterLanguageModel,
    "huggingface": HuggingFaceLanguageModel,
}


def language_model_factory(config: AppConfig):
    cls = _PROVIDERS.get(config.model_provider)
    if cls is None:
        raise ValueError(
            f"Unknown MODEL_PROVIDER={config.model_provider!r}; "
            f"expected one of {sorted(_PROVIDERS)}"
        )
    return cls.create(config)


__all__ = [
    "OpenAILanguageModel",
    "AnthropicLanguageModel",
    "OpenRouterLanguageModel",
    "HuggingFaceLanguageModel",
    "LanguageModel",
    "language_model_factory",
]
