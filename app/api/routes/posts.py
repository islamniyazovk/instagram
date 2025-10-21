from . import get_db, Depends, AsyncSession, JSONResponse, APIRouter, basic_prefix
from app.schemas.post import PostCreateRequest
from app.models.post import Post
from app.repositories.post_repository import PostRepository
from ..deps import check_auth

posts_router = APIRouter(
    prefix=f"{basic_prefix}/posts",
    tags=["posts"]
)

@posts_router.post("/create")
async def create_post(post_data: PostCreateRequest, db: AsyncSession = Depends(get_db), token = Depends(check_auth))-> \
        JSONResponse:
    pass
    # repos = PostRepository(db)
    # post = Post(**post_data.dict())

    # try:
    #     post = await repos.create(post)

