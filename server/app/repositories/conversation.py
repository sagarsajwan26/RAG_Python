from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.conversation import Conversation


class ConversationRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, tenant_id: int, user_id: int) -> Conversation:
        conversation = Conversation(tenant_id=tenant_id, user_id=user_id)
        self.db.add(conversation)
        await self.db.flush()

        return conversation

    async def get_by_id(
        self, conversation_id: int, tenant_id: int, user_id: int
    ) -> Conversation | None:
        stmt = (
            select(Conversation)
            .where(Conversation.id == conversation_id)
            .where(Conversation.tenant_id == tenant_id)
            .where(Conversation.user_id == user_id)
        )
        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_user(
        self,
        tenant_id: int,
        user_id: int,
    ) -> list[Conversation]:
        stmt = (
            select(Conversation)
            .where(Conversation.tenant_id == tenant_id, Conversation.user_id == user_id)
            .order_by(Conversation.created_at.desc())
        )
        result = await self.db.execute(stmt)

        return result.scalars().all()

    async def update_title(
        self,
        converstaion: Conversation,
        title: str,
    ) -> Conversation:
        converstaion.title = title
        return converstaion
