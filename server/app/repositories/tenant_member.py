from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tenant_member import TenantMember


class TenantMemberRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_membership(self, user_id: int, tenant_id: int) -> TenantMember | None:
        result = await self.db.execute(
            select(TenantMember).where(
                TenantMember.tenant_id == tenant_id, TenantMember.user_id == user_id
            )
        )
        return result.scalar_one_or_none()

    async def add_member(self, user_id: int, tenant_id: int, role: str) -> TenantMember:
        membership = TenantMember(user_id=user_id, tenant_id=tenant_id, role=role)
        self.db.add(membership)
        return membership
