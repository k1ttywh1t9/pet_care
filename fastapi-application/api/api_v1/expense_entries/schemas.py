from pydantic import BaseModel

from api.api_v1.mixins import PetIdMixin, IdMixin, UserIdMixin, TimestampMixin


class ExpenseEntryBase(PetIdMixin, BaseModel):
    amount: int
    purpose: str


class ExpenseEntryCreate(ExpenseEntryBase):
    pass


class ExpenseEntryRead(IdMixin, UserIdMixin, TimestampMixin, ExpenseEntryBase):
    pass


class ExpenseEntryUpdate(ExpenseEntryCreate):
    pet_id: int | None = None
    amount: int | None = None
    purpose: str | None = None
