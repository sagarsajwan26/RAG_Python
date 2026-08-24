from sqlalchemy.ext.asyncio import AsyncSession
from app.models.chunks import Chunk
from sqlalchemy import select
from app.models.documents import Document


class ChunkRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self, document_id: int, text: str, chunk_index: int, embedding: list[float]
    ) -> Chunk:

        chunk = Chunk(
            document_id=document_id,
            text=text,
            chunk_index=chunk_index,
            embedding=embedding,
        )

        self.db.add(chunk)
        return chunk

    async def similarity_search(
        self, tenant_id: int, query_embedding: list[float], top_k: int = 5
    ) -> list[Chunk]:
        distance = Chunk.embedding.cosine_distance(query_embedding)
        stmt = (
            select(Chunk)
            .join(Document, Chunk.document_id == Document.id)
            .where(Document.tenant_id == tenant_id)
            .order_by(distance)
            .limit(top_k)
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()
