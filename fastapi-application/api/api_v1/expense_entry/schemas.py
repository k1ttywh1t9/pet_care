from datetime import datetime

from pydantic import BaseModel

from core.types import UserIdType


class ExpenseEntryBase(BaseModel):
    pet_id: int
    amount: int
    purpose: str


class ExpenseEntryCreate(ExpenseEntryBase):
    pass


class ExpenseEntryRead(ExpenseEntryBase):
    id: int
    user_id: UserIdType
    created_at: datetime
    updated_at: datetime


class ExpenseEntryUpdate(ExpenseEntryCreate):
    pet_id: int | None = None
    amount: int | None = None
    purpose: str | None = None
