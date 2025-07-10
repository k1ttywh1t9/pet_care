from typing import Annotated

from pydantic import Field

from core.types import UserIdType


class UserIdFieldMixin:
    user_id: Annotated[UserIdType, Field(gt=0)]
