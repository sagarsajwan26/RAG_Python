import asyncio

from app.services.llm.ollama import OllamaLLM


async def main():
    llm = OllamaLLM()

    answer = await llm.generate(
        question="What is 2 + 2?",
        context="Basic mathematics: two plus two equals four.",
    )

    print("\nANSWER:")
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())
