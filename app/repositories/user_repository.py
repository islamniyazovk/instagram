from app.models.user import User
from sqlalchemy import select, delete


class UserRepository:
    def __init__(self, session):
        self._session = session

    async def get_by_id(self, user_id: int) -> User:
        stmt = select(User).where(User.id == user_id)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_email(self, user_email: str) -> User:
        stmt = select(User).where(User.email == user_email)
        result = await self._session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_number(self, number: str) -> User:
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

    async def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)

        if user:
            stmt = delete(User).where(User.id == user_id)
            self._session.execute(stmt)

            return True
        else:
            return False
