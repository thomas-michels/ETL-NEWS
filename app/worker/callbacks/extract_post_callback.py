from .callback_base import CallbackInterface
from app.core.shared_schemas import EventSchema
from app.core.composer import post_composer
from app.worker.utils import payload_conversor
from app.core.configs import get_environment
from app.worker.producer import KombuProducer

_env = get_environment()

class ExtractPostCallback(CallbackInterface):
    def handle(self, message: EventSchema) -> bool:
        services = post_composer()
        if services.extract_posts(start_on=message.payload.get("start_on", 0)):
            return True
        
        return False
