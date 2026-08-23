from pydantic import BaseModel, ConfigDict


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
