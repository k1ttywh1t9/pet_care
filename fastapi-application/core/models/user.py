from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @classmethod
    async def get_db(
        cls,
        session: AsyncSession,
    ):
        yield SQLAlchemyUserDatabase(
            session=session,
            user_table=cls,
        )
