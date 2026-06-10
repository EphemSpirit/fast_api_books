from fastapi import Body
from app.models import *
from app.requests import *

BOOKS: list[Book] = [
    Book(id=1, title="It", author="Stephen King", description="Very scary!", rating=4),
    Book(id=2, title="The Odyssey", author="Homer", description="A true classic", rating=5),
    Book(id=3, title="The Divine Comedy", author="Virgil", description="Not my favorite, purgatory was rough.", rating=3),
    Book(id=4, title="Fahrenheit 451", author="Ray Bradbury", description="A chilling narrative reflected in current society.", rating=5),
    Book(id=5, title="My Antonia", author="Willa Cather", description="One of the most boring books I've ever read.", rating=2),
    Book(id=6, title="The Old Man and The Sea", author="Ernest Hemingway", description="A man, his son, and a fish. Riveting...", rating=1)
]

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book

def register_routes(app):
    @app.get("/books")
    async def read_all_books() -> list[Book]:
        return BOOKS


    @app.get("/books/{book_id}")
    async def read_book(book_id: int) -> Book | None:
        for book in BOOKS:
            if book.id == book_id:
                return book


    @app.get("/books/")
    async def read_book_by_rating(rating: int) -> list[Book]:
        books: list[Book] = []
        for book in BOOKS:
            if book.rating == rating:
                books.append(book)

        return books


    @app.post("/create-book")
    async def create_book(book_request: BookCreateRequest) -> None:
        new_book = Book(**book_request.model_dump())
        BOOKS.append(find_book_id(new_book))

