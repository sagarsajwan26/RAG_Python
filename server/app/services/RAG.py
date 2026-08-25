from app.services.retrieval import RetrievalService
from app.services.context_builder import ContextBuilder
from app.services.prompt import PromptBuilder


class RAGService:
    def __init__(
        self,
        retrieval_service: RetrievalService,
        context_builder: ContextBuilder,
        llm,
        prompt_builder: PromptBuilder,
    ):
        self.retrieval_service = retrieval_service
        self.context_builder = context_builder
        self.llm = llm
        self.prompt_builder = prompt_builder

    async def answer(self, question: str, tenant_id: int, top_k: int = 5, history=None):
        conversation_history = ""
        if history:
            conversation_history = "\n".join(
                f"{message.role}:{message.content}" for message in history
            )
        chunks = await self.retrieval_service.search(
            query=question,
            tenant_id=tenant_id,
            top_k=top_k,
        )
        context = self.context_builder.build(chunks)

        prompt = self.prompt_builder.build(
            question=question, context=context, history=conversation_history
        )
        answer = await self.llm.generate(prompt)
        return {"answer": answer, "sources": chunks}
