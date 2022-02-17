from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from ..database import Base




class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    created_date = Column(DateTime, default=func.now(), nullable=False)



class BookSchema(BaseModel):
    title: str = Field(..., min_length=2, max_length=50)
    description: str = Field(..., min_length=2, max_length=50)


class BookDB(BookSchema):
    id: int

    class Config:
        orm_mode = True