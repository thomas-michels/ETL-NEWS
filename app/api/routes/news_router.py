from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.worker.producer import KombuProducer
from app.core.shared_schemas import ResponseWithList
from app.core.configs import get_environment
from app.core.composer import news_composer
from app.core.services import NewsServices

router = APIRouter(prefix="/news", tags=["News"])


@router.get("")
def get_all_news(services: NewsServices = Depends(news_composer)):
    data = services.get_all_news()

    response = ResponseWithList(data=data)

    return JSONResponse(
        content=jsonable_encoder(response.dict()), status_code=status.HTTP_200_OK
    )
