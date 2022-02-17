from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from . import views
from .models import BookDB, BookSchema
from ..database import SessionLocal


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/", response_model=BookDB, status_code=201)
def create_book(*, db: Session = Depends(get_db), payload: BookSchema):
    book = views.post(db_session=db, payload=payload)
    return book


@router.get("/{id}/", response_model=BookDB)
def read_book(
    *, db: Session = Depends(get_db), id: int = Path(..., gt=0),
):
    book = views.get(db_session=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get("/", response_model=List[BookDB])
def all_books(db: Session = Depends(get_db)):
    return views.get_all(db_session=db)


@router.put("/{id}/", response_model=BookDB)
def update_book(
    *, db: Session = Depends(get_db), id: int = Path(..., gt=0), payload: BookSchema
):
    book = views.get(db_session=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book = views.put(
        db_session=db, book=book, title=payload.title, description=payload.description
    )
    return book


@router.delete("/{id}/", response_model=BookDB)
def delete_book(
    *, db: Session = Depends(get_db), id: int = Path(..., gt=0),
):
    book = views.get(db_session=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book = views.delete(db_session=db, id=id)
    return book