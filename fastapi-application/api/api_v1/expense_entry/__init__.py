from fastapi import APIRouter
from .views import router as views_router


router = APIRouter(
    tags=["Expense entries"],
)


router.include_router(
    router=views_router,
)
