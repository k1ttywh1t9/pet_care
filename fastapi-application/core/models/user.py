from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base
from .mixins.id_int_pk import IdIntPkMixin
from core.types import UserIdType


class User(IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType], Base):

    @classmethod
    def get_db(
        cls,
        session: AsyncSession,
    ):
        return SQLAlchemyUserDatabase(
            session=session,
            user_table=cls,
        )
