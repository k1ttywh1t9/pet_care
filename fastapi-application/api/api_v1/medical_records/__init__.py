from fastapi import APIRouter

from .views import router as views_router


router = APIRouter(
    tags=["Medical records"],
)

router.include_router(
    router=views_router,
)
