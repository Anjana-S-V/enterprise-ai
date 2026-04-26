from app.core.config import settings
from app.services.mock_ai_service import MockAIService
from app.services.ai_service import BaseAIService


def get_ai_service() -> BaseAIService:
    if settings.AI_PROVIDER == "mock":
        return MockAIService()

    raise ValueError(f"Unsupported AI provider: {settings.AI_PROVIDER}")