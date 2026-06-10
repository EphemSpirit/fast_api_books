from typing import Optional

class Book:
    id: Optional[int] = None
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, title, author, description, rating, id = None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
