from fastapi import APIRouter

from .pet_image_handler import router as pet_image_router
from .pet_medical_document_handler import router as medical_record_document_router


router = APIRouter()

router.include_router(
    pet_image_router,
)
router.include_router(
    router=medical_record_document_router,
)
