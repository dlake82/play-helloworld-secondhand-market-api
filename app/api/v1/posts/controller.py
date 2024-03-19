from fastapi import APIRouter, Depends

from app.api.error import Exception404, Exception500
from app.api.v1.posts.schema import DeletePostRes, PaginationPostRes
from app.crud.crud import CRUD
from app.db.session import get_crud
from app.models.post import Post
from app.schemas.base import CreatedRes
from app.schemas.post import PostCreate, PostUpdate

router = APIRouter(prefix="/posts")


@router.get("/")
async def post(id: int, crud: CRUD = Depends(get_crud)) -> Post:
    """게시글 정보를 보내줌

    Args:
        id (int): 게시글 아이디
        crud (CRUD, optional): 디비

    Returns:
        post: 게시글
    """

    post = crud.post.get_by_id(id=id)

    if not post:
        raise Exception404(type="postDoesNotExists")

    return post


@router.get("/list")
async def pagination(
    crud: CRUD = Depends(get_crud), *, page: int = 0, limit: int = 10
) -> PaginationPostRes:
    """게시글 목록을 보여주기 위해 게시글의 페이징 메타 데이터, 게시글 리스트를 반환함

    Args:
        db (Session, optional): db 세션
        page (int, optional): 페이지네이션 요청 페이지
        limit (int, optional): 한 페이지 아이템 수

    Returns:
        GetpostByPaginationRes: 페이징 메타 데이터, 게시글 리스트
    """
    post_count = crud.post.get_count()
    post_list = crud.post.get_by_pagination(
        skip=page * limit, limit=(page + 1) * limit
    )

    return PaginationPostRes(
        limit=limit,
        total_count=post_count,
        total_page_count=(post_count - 1) // limit + 1,
        post_list=post_list,
    )


@router.post("/")
def create(
    post_create: PostCreate, *, crud: CRUD = Depends(get_crud)
) -> CreatedRes:
    """게시글을 생성한다.

    Args:
        post_create (postCreate): 생성할 게시글
        crud (CRUD, optional): 디비

    Returns:

        CreatedRes: 생성 성공
    """
    crud.post.create_post(post_create)

    return CreatedRes(msg="Success to create post.")


@router.put("/")
def update(post_update: PostUpdate, *, crud: CRUD = Depends(get_crud)) -> Post:
    updated_post = crud.post.update_post(post_update)

    return updated_post


@router.post("/")
def delete(req: DeletePostRes, *, crud: CRUD = Depends(get_crud)):
    """게시글들을 삭제한다.

    Args:
        req (DeletepostsReq): 게시글 아이디 리스트
        crud (CRUD, optional): 디비

    Returns:
        DefaultRes: 게시글 성공 메세지, 리턴
    """
    id_list = req.id_list
    ret_list = [crud.post.remove(id=id) for id in id_list]

    if len(ret_list) != len(id_list):
        Exception500(type="FailedToDeletepost")

    return True
