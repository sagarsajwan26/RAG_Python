from fastapi import Depends, HTTPException, status

from app.core.tenant import get_current_tenant_member
from app.models.tenant_member import TenantMember


async def require_document_upload_permission(
    membership: TenantMember = Depends(get_current_tenant_member),
) -> TenantMember:

    if membership.role not in {"owner", "admin"}:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to upload documents",
        )

    return membership
