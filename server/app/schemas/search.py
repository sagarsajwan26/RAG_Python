from pydantic import BaseModel, Field


class SearchRequest(BaseModel):

    query: str = Field(min_length=2)
    top_k: int = Field(default=5, ge=1, le=20)


class SearchResult(BaseModel):
    id: int
    document_id: int
    chunk_index: int
    text: str


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]
