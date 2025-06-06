from typing import TYPE_CHECKING
from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
    async_scoped_session,
)

from core.config import settings


if TYPE_CHECKING:
    from collections.abc import AsyncGenerator


class DatabaseHelper:
    def __init__(self, config: dict):
        self.engine: AsyncEngine = create_async_engine(**config)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> "AsyncGenerator[AsyncSession, None]":
        async with self.session_factory() as session:
            yield session

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def scoped_session_dependency(self):
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    settings.db.model_dump(),
)
