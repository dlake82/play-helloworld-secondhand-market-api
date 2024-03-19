from datetime import datetime

from sqlmodel import SQLModel


class PostCreate(SQLModel):
    name: str
    author: str
    description: str
    images: list[str]
    updated_at: datetime
    created_at: datetime


class PostUpdate(PostCreate):
    pass


class PostBase(PostCreate):
    id: int
