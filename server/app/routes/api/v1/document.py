from fastapi import APIRouter, Depends, File, UploadFile, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.dependencies import get_db
from app.models.tenant_member import TenantMember
from app.models.user import User
from app.schemas.document import DocumentResponse
from app.services.document import DocumentService
from app.core.permission import require_document_upload_permission
from pathlib import Path
from app.core.authorization import require_roles

router = APIRouter()


@router.post(
    "/{tenant_id}/documents",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_document(
    tenant_id: int,
    file: UploadFile = File(...),
    membership: TenantMember = Depends(require_roles("owner", "admin")),
    db: AsyncSession = Depends(get_db),
):
    service = DocumentService(db)

    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename is required",
        )
    allowed_extensions = {".pdf", ".txt"}
    extension = Path(file.filename).suffix.lower()
    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF and TXT files are supported",
        )

    storage_path = await service.storage.save(file=file, tenant_id=membership.tenant_id)
    document = await service.process_document(
        tenant_id=membership.tenant_id,
        filename=file.filename,
        uploaded_by=membership.user_id,
        storage_path=storage_path,
    )
    return document
