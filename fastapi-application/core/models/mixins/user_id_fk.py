from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.types import UserIdType


class UserIdFkMixin:
    user_id: Mapped[UserIdType] = mapped_column(
        ForeignKey(
            "user.id",
            ondelete="SET NULL",
        ),
    )
