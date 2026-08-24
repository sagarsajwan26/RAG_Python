from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.documents import Document


class DocumentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(
        self,
        tenant_id: int,
        filename: str,
        uploaded_by: int,
        storage_path: str,
    ) -> Document:
        document = Document(
            tenant_id=tenant_id,
            filename=filename,
            uploaded_by=uploaded_by,
            storage_path=storage_path,
        )

        self.db.add(document)
        await self.db.flush()
        return document

    async def get_by_id(self, document_id: int, tenant_id: int) -> Document | None:
        result = await self.db.execute(
            select(Document).where(
                Document.id == document_id, Document.tenant_id == tenant_id
            )
        )
        return result.scalar_one_or_none()

    async def get_by_tenant(self, tenant_id: int) -> list[Document]:
        result = await self.db.execute(
            select(Document)
            .where(Document.tenant_id == tenant_id)
            .order_by(Document.created_at.desc())
        )

        return list(result.scalars().all())
