from datetime import datetime
from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
