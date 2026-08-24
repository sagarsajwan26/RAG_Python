from fastapi import APIRouter, Depends, HTTPException, status
from app.core.tenant import get_current_tenant_member
from app.models.tenant_member import TenantMember
from app.core.dependencies import get_current_user
from app.database.dependencies import get_db
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.tenant import TenantCreate, TenantResponse
from app.services.tenant import TenantService

router = APIRouter()


@router.get("/{tenant_id}/text")
async def test_tenant_access(
    membership: TenantMember = Depends(get_current_tenant_member),
):
    return {
        "message": "Tenant access granted",
        "tenant_id": membership.tenant_id,
        "user_id": membership.user_id,
        "role": membership.role,
    }


@router.post("/", response_model=TenantResponse, status_code=status.HTTP_201_CREATED)
async def create_tenant(
    data: TenantCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    service = TenantService(db)

    try:
        return await service.create_tenant(
            user_id=current_user.id,
            name=data.name,
            slug=data.slug,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
