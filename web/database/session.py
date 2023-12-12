import asyncio
from typing import Generator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from web.config import DATABASE_URL
from web.database.dals import UserDAL
from web.database.models import Base

engine = create_async_engine(DATABASE_URL, future=True, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> Generator:
    """Dependency for getting async session"""
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()


async def main():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def test():
    async with async_session() as session:
        user = await UserDAL.get(session, 'ramisram1s')
        print(user)


if __name__ == '__main__':
    asyncio.run(main())
