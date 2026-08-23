from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_current_user
from app.database.dependencies import get_db
from app.models.tenant_member import TenantMember
from app.models.user import User
from app.repositories.tenant_member import TenantMemberRepository


async def get_current_tenant_member(
    tenant_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> TenantMember:
    repository = TenantMemberRepository(db)
    membership = await repository.get_membership(
        user_id=current_user.id, tenant_id=tenant_id
    )
    if membership is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is not a member of this tenant",
        )

    return membership
