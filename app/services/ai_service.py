from abc import ABC, abstractmethod


class BaseAIService(ABC):

    @abstractmethod
    async def analyze(self, text: str) -> dict:
        pass