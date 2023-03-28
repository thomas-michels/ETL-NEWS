from .callback_base import CallbackInterface
from app.core.shared_schemas import EventSchema
from app.core.composer import post_composer


class ExtractCallback(CallbackInterface):
    def handle(self, message: EventSchema) -> bool:
        services = post_composer()
        return services.start_extract(start_page=message.payload.get("start", 0))
