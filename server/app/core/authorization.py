from fastapi import Depends, HTTPException, status
from app.core.tenant import get_current_tenant_member
from app.models.tenant_member import TenantMember


def require_roles(*allowed_roles: str):
    async def dependency(
        membership: TenantMember = Depends(get_current_tenant_member),
    ) -> TenantMember:
        if membership.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permission"
            )
        return membership

    return dependency
