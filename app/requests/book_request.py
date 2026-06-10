from pydantic import BaseModel, Field

class BookCreateRequest(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=5)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)