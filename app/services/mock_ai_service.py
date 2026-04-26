class MockAIService:
    async def analyze(self, text: str) -> dict:
        return {
            "length": len(text),
            "uppercase": text.upper()
        }