from .callback_base import CallbackInterface
from app.core.shared_schemas import EventSchema


class ExtractCallback(CallbackInterface):

    def handle(self, message: EventSchema) -> bool:
        return super().handle(message)
