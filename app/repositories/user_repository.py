from app.models.user import User
from . import AsyncSession, select, delete


class UserRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_id(self, user_id: int) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_email(self, user_email: str) -> User | None:
        stmt = select(User).where(User.email == user_email)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_number(self, number: str) -> User | None:
        stmt = select(User).where(User.number == number)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def create(self, user: User) -> User:
        self._session.add(user)

        await self._session.flush()
        return user

    async def update(self, user_id: int, **fields) -> User:
        user = await self.get_by_id(user_id)

        for key, value in fields.items():
            setattr(user, key, value)

        await self._session.flush()
        return user

    async def delete(self, user_id: int) -> None:
        stmt = delete(User).where(User.id == user_id)
        await self._session.execute(stmt)
