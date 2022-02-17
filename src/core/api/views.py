from sqlalchemy.orm import Session

from .models import Book, BookSchema


def post(db_session: Session, payload: BookSchema):
    book = Book(title=payload.title, description=payload.description)
    db_session.add(book)
    db_session.commit()
    db_session.refresh(book)
    return book


def get(db_session: Session, id: int):
    return db_session.query(Book).filter(Book.id == id).first()


def get_all(db_session: Session):
    return db_session.query(Book).all()


def put(db_session: Session, book: Book, title: str, description: str):
    book.title = title
    book.description = description
    db_session.commit()
    return book


def delete(db_session: Session, id: int):
    book = db_session.query(Book).filter(Book.id == id).first()
    db_session.delete(book)
    db_session.commit()
    return book