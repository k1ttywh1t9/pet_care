from fastapi import APIRouter

from .pet_image_handler import router as pet_image_router


router = APIRouter()

router.include_router(pet_image_router)
