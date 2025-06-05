from fastapi import APIRouter
from .views import router as views_router

router = APIRouter(
    tags=["Pets"],
)
router.include_router(
    router=views_router,
)
