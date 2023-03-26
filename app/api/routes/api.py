from fastapi import APIRouter
from .extract_routes import router as extract_router


router = APIRouter()
router.include_router(extract_router)
