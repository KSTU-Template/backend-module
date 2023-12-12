from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from web.database.models import User


class UserDAL:
    @staticmethod
    async def create(db_session: AsyncSession, username: str, password: str) -> User:
        new_user = User(username=username, password=password)
        db_session.add(new_user)
        await db_session.commit()

        return new_user

    @staticmethod
    async def read(db_session: AsyncSession, **kwargs) -> User | list[User]:
        stmt = select(User).filter_by(**kwargs)
        users = await db_session.scalars(stmt)

        return users.fetchall()

    @staticmethod
    async def get(db_session: AsyncSession, username: str) -> User:
        stmt = select(User).filter_by(username=username)
        user = await db_session.scalar(stmt)

        return user
