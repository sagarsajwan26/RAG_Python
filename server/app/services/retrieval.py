from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.chunks import Chunk
from app.models.documents import Document
from app.repositories.chunk import ChunkRepository


class RetrievalService:
    def __init__(
        self, db: AsyncSession, embedding_model, chunk_repository: ChunkRepository
    ):
        self.db = db
        self.embedding_model = embedding_model
        self.chunk_repository = chunk_repository

    async def search(self, query: str, tenant_id: int, top_k: int = 5):
        query_embedding = self.embedding_model.embed(query)
        chunks = await self.chunk_repository.similarity_search(
            tenant_id=tenant_id, query_embedding=query_embedding, top_k=top_k
        )
        return chunks
