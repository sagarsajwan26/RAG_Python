from pydantic import BaseModel, Field
from datetime import datetime


class AskRequest(BaseModel):
    question: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=10)


class SourceResponse(BaseModel):
    id: int
    document_id: int
    chunk_index: int
    text: str


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[SourceResponse]


class ConversationCreateResponse(BaseModel):

    id: int


class MessageResponse(BaseModel):
    id: int
    role: str
    content: str


class ConversationResponse(BaseModel):
    id: int
    messages: list[MessageResponse]


class ConversationListItem(BaseModel):
    id: int
    created_at: datetime
    title: str | None


class ConversationListResponse(BaseModel):
    conversations: list[ConversationListItem]
