from abc import ABC, abstractmethod


class BaseLLM(ABC):
    @abstractmethod
    async def generate(
        self,
        question: str,
        context: str,
    ) -> str:
        pass
