from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime

from database.session import create_db_and_tables, get_session
from models.book import Book, BookCreate, BookUpdate

app = FastAPI(
    title="Book Inventory API",
    version="1.0.0",
    description="A simple CRUD API for managing a bookstore inventory."
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# CREATE A NEW BOOK
@app.post("/books", response_model=Book, status_code=201)
def create_book(
    book: BookCreate,
    session: Session = Depends(get_session)
):
    db_book = Book.model_validate(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


# LIST ALL BOOKS (OPTIONAL FILTERS)
@app.get("/books", response_model=List[Book])
def get_books(
    author: Optional[str] = None,
    available: Optional[bool] = None,
    session: Session = Depends(get_session)
):
    statement = select(Book)

    if author:
        statement = statement.where(Book.author.contains(author))

    if available is not None:
        statement = statement.where(Book.available == available)

    books = session.exec(statement).all()
    return books


# SEARCH BOOKS BY TITLE OR AUTHOR
@app.get("/books/search", response_model=List[Book])
def search_books(
    query: str = Query(..., description="Search by title or author"),
    session: Session = Depends(get_session)
):
    statement = select(Book).where(
        Book.title.contains(query) |
        Book.author.contains(query)
    )

    books = session.exec(statement).all()
    return books


# GET A SINGLE BOOK BY ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


# UPDATE A BOOK
@app.patch("/books/{book_id}", response_model=Book)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = book_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(book, key, value)

    book.updated_at = datetime.utcnow()

    session.add(book)
    session.commit()
    session.refresh(book)

    return book


# DELETE A BOOK
@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    session: Session = Depends(get_session)
):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)
    session.commit()

    return {"message": "Book deleted successfully"}