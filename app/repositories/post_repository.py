from . import AsyncSession, select, delete
from app.models.post import Post


class PostRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, post_id: int) -> Post:
        stmt = select(Post).where(Post.id == post_id)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def create(self, post: Post) -> Post:
        self._session.add(post)

        await self._session.flush()
        return post

    async def update(self, post_id, **fields) -> Post:
        post = await self.get_by_id(post_id)
        for key, value in fields.items():
            setattr(post, key, value)

        await self._session.flush()
        return post

    async def delete(self, post_id: int) -> None:
        stmt = delete(Post).where(Post.id == post_id)
        await self._session.execute(stmt)
