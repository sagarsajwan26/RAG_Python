from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.dependencies import get_db
from app.core.authorization import require_roles
from app.models.tenant_member import TenantMember

from app.repositories.chunk import ChunkRepository
from app.services.embedding import EmbeddingService
from app.services.retrieval import RetrievalService
from app.services.context_builder import ContextBuilder
from app.services.prompt import PromptBuilder
from app.services.RAG import RAGService
from app.services.llm.ollama import OllamaLLM
from app.schemas.conversation import AskRequest, AskResponse

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
async def ask(
    request: AskRequest,
    membership: TenantMember = Depends(require_roles("owner", "admin", "member")),
    db: AsyncSession = Depends(get_db),
):

    chunk_repository = ChunkRepository(db)
    embedding_service = EmbeddingService()
    retrieval_service = RetrievalService(
        db=db, embedding_model=embedding_service, chunk_repository=chunk_repository
    )
    context_builder = ContextBuilder()
    prompt_builder = PromptBuilder()
    llm = OllamaLLM()
    rag_service = RAGService(
        retrieval_service=retrieval_service,
        context_builder=context_builder,
        prompt_builder=prompt_builder,
        llm=llm,
    )

    result = await rag_service.answer(
        question=request.question,
        tenant_id=membership.tenant_id,
        top_k=request.top_k,
    )
    return {
        "question": request.question,
        "answer": result["answer"],
        "source": [
            {
                "id": chunk.id,
                "document_id": chunk.document_id,
                "chunk_index": chunk.chunk_index,
                "text": chunk.text,
            }
            for chunk in result["sources"]
        ],
    }
