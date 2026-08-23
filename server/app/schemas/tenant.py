from pydantic import BaseModel, Field


class TenantCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    slug: str = Field(min_length=1, max_length=100)


class TenantResponse(BaseModel):
    id: int
    name: str
    slug: str
    model_config = {"from_attributes": True}
