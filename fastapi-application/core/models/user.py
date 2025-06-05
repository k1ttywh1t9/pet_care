from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .mixins.id_int_pk import IdIntPkMixin
from core.types import UserIdType

if TYPE_CHECKING:
    from .pet import Pet


class User(IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType], Base):
    pets: Mapped[list["Pet"]] = relationship(back_populates="owner")

    @classmethod
    def get_db(
        cls,
        session: AsyncSession,
    ):
        return SQLAlchemyUserDatabase(
            session=session,
            user_table=cls,
        )
