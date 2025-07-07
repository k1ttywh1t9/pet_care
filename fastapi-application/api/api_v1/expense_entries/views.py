from fastapi import APIRouter

from api.api_v1.expense_entries.schemas import (
    ExpenseEntryCreate,
    ExpenseEntryRead,
    ExpenseEntryUpdate,
)
from core.models import ExpenseEntry
from crud_router import CRUDRouterFactory

router = APIRouter()

crud_router = CRUDRouterFactory(
    model=ExpenseEntry,
).get_router(
    create_schema=ExpenseEntryCreate,
    read_schema=ExpenseEntryRead,
    update_schema=ExpenseEntryUpdate,
)

router.include_router(router=crud_router)
