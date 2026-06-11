from typing import Optional
from pydantic import BaseModel


class Book(BaseModel):
    id: Optional[int] = None # required in update request
    title: str
    author: str
    description: str
    rating: int
    published_date: int
