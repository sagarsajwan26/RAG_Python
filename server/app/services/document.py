from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.document import DocumentRepository
from app.repositories.chunk import ChunkRepository
from app.services.document_parser import DocumentParser
from app.services.chunkers import TextChunker
from app.services.embedding import EmbeddingService
from app.services.storage import StorageService


class DocumentService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.document_repository = DocumentRepository(db)
        self.storage = StorageService()
        self.chunk_repository = ChunkRepository(db)
        self.parser = DocumentParser()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()

    # async def create_document(self, tenant_id: int, filename: str, uploaded_by: int):
    #     document = await self.document_repository.create(
    #         tenant_id=tenant_id, filename=filename, uploaded_by=uploaded_by
    #     )
    #     await self.db.commit()
    #     await self.db.refresh(document)
    #     return document

    async def process_document(
        self,
        tenant_id: int,
        filename: str,
        storage_path: str,
        uploaded_by: int,
    ):
        document = await self.document_repository.create(
            tenant_id=tenant_id,
            filename=filename,
            storage_path=storage_path,
            uploaded_by=uploaded_by,
        )
        text = self.parser.extract_text(storage_path)
        chunks = self.chunker.split(text)

        for index, chunk_text in enumerate(chunks):
            embedding = self.embedding_service.embed(chunk_text)
            print("Chunk:", index)
            print("Embedding type:", type(embedding))
            print("Embedding dimensions:", len(embedding))
            await self.chunk_repository.create(
                document_id=document.id,
                text=chunk_text,
                chunk_index=index,
                embedding=embedding,
            )
        document.status = "processed"
        await self.db.commit()
        await self.db.refresh(document)

        return document
