from typing import Annotated
from pydantic import Field


class IdFieldMixin:
    id: Annotated[int, Field(gt=0)]
