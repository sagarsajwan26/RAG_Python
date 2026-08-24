from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=10)


class SourceResponse(BaseModel):
    id: int
    document_id: int
    chunk_inded: int
    text: str


class AskResponse(BaseModel):
    question: str
    answer: str
    source: list[SourceResponse]
