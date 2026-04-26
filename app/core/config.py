import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "Enterprise AI"
    APP_VERSION: str = "1.0.0"
    AI_PROVIDER: str = os.getenv("AI_PROVIDER", "mock")
    PORT: int = int(os.getenv("PORT", 8000))


settings = Settings()