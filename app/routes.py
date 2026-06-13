from fastapi import Path, Query, HTTPException
from starlette import status
from app.models import *
from app.requests import *

BOOKS: list[Book] = [
    Book(id=1, title="It", author="Stephen King", description="Very scary!", rating=4, published_date=1986),
    Book(id=2, title="The Odyssey", author="Homer", description="A true classic", rating=5, published_date=725),
    Book(id=3, title="The Divine Comedy", author="Virgil", description="Not my favorite, purgatory was rough.", rating=3, published_date=20),
    Book(id=4, title="Fahrenheit 451", author="Ray Bradbury", description="A chilling narrative reflected in current society.", rating=5, published_date=1953),
    Book(id=5, title="My Antonia", author="Willa Cather", description="One of the most boring books I've ever read.", rating=2, published_date=1318),
    Book(id=6, title="The Old Man and The Sea", author="Ernest Hemingway", description="A man, his son, and a fish. Riveting...", rating=1, published_date=1952)
]

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book

def register_routes(app):
    @app.get("/books", status_code=status.HTTP_200_OK)
    async def read_all_books() -> list[Book]:
        return BOOKS


    @app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
    async def read_book(book_id: int = Path(gt=0)) -> Book:
        for book in BOOKS:
            if book.id == book_id:
                return book
        raise HTTPException(status_code=404, detail="Item not found")


    @app.get("/books/", status_code=status.HTTP_200_OK)
    async def read_book_by_rating(rating: int = Query(gt=0, lt=6)) -> list[Book]:
        books: list[Book] = []
        for book in BOOKS:
            if book.rating == rating:
                books.append(book)

        return books

    @app.get("/book/publish/", status_code=status.HTTP_200_OK)
    async def read_book_by_publish_date(published_date: int = Query(gt=-1)) -> list[Book]:
        books: list[Book] = []
        for book in BOOKS:
            if book.published_date == published_date:
                books.append(book)

        return books


    @app.post("/create-book", status_code=status.HTTP_201_CREATED)
    async def create_book(book_request: BookRequest) -> None:
        new_book = Book(**book_request.model_dump())
        BOOKS.append(find_book_id(new_book))


    @app.put("/books/update", status_code=status.HTTP_204_NO_CONTENT)
    async def update_book(book: BookRequest) -> None:
        book_changed = False
        for i in range(len(BOOKS)):
            if BOOKS[i].id == book.id:
                BOOKS[i] = book
                book_changed = True

        if not book_changed:
            raise HTTPException(status_code=404, detail="Item not found")



    @app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_book(book_id: int = Path(gt=0)) -> None:
        book_deleted = False
        for i in range(len(BOOKS)):
            if BOOKS[i].id == book_id:
                BOOKS.pop(i)
                book_deleted = True
                break

        if not book_deleted:
            raise HTTPException(status_code=404, detail="Item not found")