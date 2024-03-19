from app.api.error import Exception404
from app.api.v1.posts.schema import PaginationPostRes
from app.crud.crud import CRUD
from app.models.post import Post


async def get_preset_pagination_from_crud(
    crud: CRUD,
    *,
    page: int = 0,
    limit: int = 10,
) -> PaginationPostRes:
    preset_count = crud.preset.get_count()
    preset_list = crud.preset.get_by_pagination(
        skip=page * limit, limit=(page + 1) * limit
    )

    return PaginationPostRes(
        limit=limit,
        total_count=preset_count,
        total_page_count=(preset_count - 1) // limit + 1,
        preset_list=preset_list,
    )
