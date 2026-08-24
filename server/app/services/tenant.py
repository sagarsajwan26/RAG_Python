from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.tenant import TenantRepository
from app.repositories.tenant_member import TenantMemberRepository


class TenantService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.tenant_repository = TenantRepository(db)
        self.tenant_member_repository = TenantMemberRepository(db)

    async def create_tenant(
        self,
        user_id: int,
        name: str,
        slug: str,
    ):
        existing_tenant = await self.tenant_repository.get_by_slug(slug)
        if existing_tenant is not None:
            raise ValueError("tenant slug already exists")

        tenant = await self.tenant_repository.create(name=name, slug=slug)
        await self.tenant_member_repository.add_member(
            user_id=user_id, tenant_id=tenant.id, role="owner"
        )
        # membership = TenantMember(user_id=user_id, tenant_id=tenant.id, role="owner")
        # self.db.add(membership)
        await self.db.commit()
        await self.db.refresh(tenant)
        return tenant
