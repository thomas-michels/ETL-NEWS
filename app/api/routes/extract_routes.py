from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.worker.producer import KombuProducer
from app.core.shared_schemas import EventSchema
from app.core.configs import get_environment

_env = get_environment()

router = APIRouter(prefix="/extract", tags=["Extract"])


@router.post("/start")
def start_extract_data():
    message = EventSchema(
        sended_to=_env.EXTRACT_CHANNEL,
        payload={}
    )

    producer = KombuProducer()
    producer.send_messages(message=message)

    return JSONResponse(
        content={"message": "Extract will be started"}, status_code=status.HTTP_202_ACCEPTED
    )
