from .callback_base import CallbackInterface
from app.core.shared_schemas import EventSchema
from app.core.composer import post_composer


class PopulateNewsCallback(CallbackInterface):
    def handle(self, message: EventSchema) -> bool:
        ...
