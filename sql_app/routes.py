# routes.py

from fastapi import APIRouter, HTTPException, Depends, Path
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, Request, Response, RequestBook
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/books/create", response_model=Response)
async def create_book(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(status="Ok", code="200", message="Book created successfully")

@router.get("/books", response_model=Response)
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=books)

@router.patch("/books/{book_id}", response_model=Response)
async def update_book(book_id: int, request: RequestBook, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id=book_id, title=request.parameter.title, description=request.parameter.description)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status="Ok", code="200", message="Success update data", result=book)

@router.delete("/books/{book_id}", response_model=Response)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=book_id)
    return Response(status="Ok", code="200", message="Success delete data")
