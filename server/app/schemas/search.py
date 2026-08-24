from pydantic import BaseModel, ConfigDict


class SearchRequest(BaseModel):

    query: str
    top_k: int = 5


class SearchResult(BaseModel):
    id: int
    document_id: int
    chunk_index: int
    text: str


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]
