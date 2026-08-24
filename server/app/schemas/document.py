from datetime import datetime
from pydantic import BaseModel, ConfigDict


class DocumentResponse(BaseModel):

    id: int
    tenant_id: int
    filename: str
    uploaded_by: int
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DocumentCreate(BaseModel):
    filename: str
