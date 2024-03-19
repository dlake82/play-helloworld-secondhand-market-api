from datetime import datetime

from sqlalchemy import Column, String, Text
from sqlmodel import Field

from app.models.base import Base


class Post(Base, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str = Field()
    author: str = Field()
    description: str = Field()
    images: list[str] = Field()
    updated_at: datetime | None = Field(nullable=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
