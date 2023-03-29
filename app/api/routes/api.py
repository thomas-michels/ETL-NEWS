from fastapi import APIRouter
from .extract_routes import router as extract_router
from .news_router import router as news_router


router = APIRouter()
router.include_router(extract_router)
router.include_router(news_router)
