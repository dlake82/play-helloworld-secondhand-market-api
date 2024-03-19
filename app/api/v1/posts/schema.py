from sqlmodel import SQLModel

from app.models.post import Post
from app.schemas.post import PostBase


class GetPost(PostBase):
    pass


class PaginationPostRes(SQLModel):
    limit: int
    total_count: int
    total_page_count: int
    preset_list: list[Post]


class DeletePostRes(SQLModel):
    id_list: list[int]
