from pydantic import BaseModel, Field

class BookCreateRequest(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=5)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "It",
                "author": "Stephen King",
                "description": "Gave me a fear of clowns",
                "rating": 4
            }
        }
    }