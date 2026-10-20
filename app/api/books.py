from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db import crud
from app.db.db import get_db
from app.schemas import BookCreate, BookResponse, BookUpdate

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[BookResponse])
def get_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    if category_id:
        return crud.get_books_by_category(db, category_id)
    return crud.get_all_books(db)

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Проверка бизнес-логики: существует ли категория
    if not crud.get_category(db, book.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")
    return crud.create_book(db, book.title, book.description, book.price, book.url, book.category_id)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    b = crud.get_book(db, book_id)
    if not b:
        raise HTTPException(status_code=404, detail="Book not found")
    return b

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    if not crud.get_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    if book_data.category_id and not crud.get_category(db, book_data.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")
    # Исключаем None значения, чтобы не перезаписать данные пустотой
    update_data = book_data.model_dump(exclude_unset=True)
    return crud.update_book(db, book_id, **update_data)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")