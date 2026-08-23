from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.search import SearchRequest
from app.services.retrieval import RetrievalService
from app.database.dependencies import get_db
from app.core.authorization import require_roles
from app.models.tenant_member import TenantMember
from app.services.retrieval import RetrievalService
from app.services.embedding import EmbeddingService
from app.repositories.chunk import ChunkRepository
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/search")
async def search(
    tenant_id: int,
    query: str,
    membership: TenantMember = Depends(require_roles("owner", "admin", "members")),
    db: AsyncSession = Depends(get_db),
):
    chunk_repository = ChunkRepository(db)
    embedding_model = EmbeddingService()
    service = RetrievalService(
        db=db, embedding_model=embedding_model, chunk_repository=chunk_repository
    )

    chunks = await service.search(query=query, tenant_id=membership.tenant_id, top_k=5)
    return {
        "query": query,
        "result": [
            {
                "id": chunk.id,
                "document_id": chunk.document_id,
                "chunk_index": chunk.chunk_index,
                "text": chunk.text,
            }
            for chunk in chunks
        ],
    }
