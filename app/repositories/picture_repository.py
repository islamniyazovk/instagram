from . import AsyncSession
from ..models.picture import Picture


class PostRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, picture: Picture) -> Picture:
        self._session.add(picture)
        await self._session.flush()

        return picture
