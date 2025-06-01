from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
    async_engine_from_config,
)

from core.config import settings


class DatabaseHelper:
    def __init__(self, config: dict):
        self.engine: AsyncEngine = async_engine_from_config(config)
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )


db_helper = DatabaseHelper(
    settings.db.model_dump(),
)
