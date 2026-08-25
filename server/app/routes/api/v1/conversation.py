from fastapi import APIRouter, Depends, HTTPException, status
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
from app.schemas.conversation import (
    AskRequest,
    AskResponse,
    ConversationCreateResponse,
    ConversationListResponse,
    ConversationResponse,
)
from app.repositories.conversation import ConversationRepository
from app.repositories.message import MessageRepository

router = APIRouter()


@router.post("/{conversation_id}/ask", response_model=AskResponse)
async def ask(
    conversation_id: int,
    request: AskRequest,
    membership: TenantMember = Depends(require_roles("owner", "admin", "member")),
    db: AsyncSession = Depends(get_db),
):

    conversation_repository = ConversationRepository(db)
    message_repository = MessageRepository(db)

    conversation = await conversation_repository.get_by_id(
        conversation_id=conversation_id,
        tenant_id=membership.tenant_id,
        user_id=membership.user_id,
    )
    if conversation is None:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    if conversation.title is None:
        conversation.title = request.question[:255]
    messages = await message_repository.get_by_conversation(conversation_id)
    await message_repository.create(
        conversation_id=conversation_id, role="user", content=request.question
    )
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
        history=messages,
    )

    await message_repository.create(
        conversation_id=conversation_id, role="assistant", content=result["answer"]
    )

    await db.commit()
    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": [
            {
                "id": chunk.id,
                "document_id": chunk.document_id,
                "chunk_index": chunk.chunk_index,
                "text": chunk.text,
            }
            for chunk in result["sources"]
        ],
    }


@router.post("/", response_model=ConversationCreateResponse)
async def create_conversation(
    membership: TenantMember = Depends(require_roles("owner", "admin", "member")),
    db: AsyncSession = Depends(get_db),
):
    repository = ConversationRepository(db)
    conversation = await repository.create(
        tenant_id=membership.tenant_id,
        user_id=membership.user_id,
    )

    await db.commit()

    return {"id": conversation.id}


@router.get("/", response_model=ConversationListResponse)
async def get_conversations(
    membership: TenantMember = Depends(require_roles("owner", "admin", "member")),
    db: AsyncSession = Depends(get_db),
):
    repository = ConversationRepository(db)
    conversations = await repository.get_by_user(
        tenant_id=membership.tenant_id, user_id=membership.user_id
    )

    return {
        "conversations": [
            {"id": conversation.id, "created_at": conversation.created_at}
            for conversation in conversations
        ]
    }


@router.get("{conversation_id}", response_model=ConversationResponse)
async def get_conversation(
    conversation_id: int,
    membership: TenantMember = Depends(require_roles("owner", "admin", "member")),
    db: AsyncSession = Depends(get_db),
):
    conversation_repository = ConversationRepository(db)
    message_repository = MessageRepository(db)

    conversation = await conversation_repository.get_by_id(
        conversation_id=conversation_id,
        tenant_id=membership.tenant_id,
        user_id=membership.user_id,
    )

    if conversation is None:
        raise HTTPException(status_code=404, detail="conversation not found")

    messages = await message_repository.get_by_conversation(conversation_id)
    return {
        "id": conversation.id,
        "messages": [
            {"id": message.id, "role": message.role, "content": message.content}
            for message in messages
        ],
    }
