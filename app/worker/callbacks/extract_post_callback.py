from .callback_base import CallbackInterface
from app.core.shared_schemas import EventSchema
from app.core.composer import post_composer


class ExtractPostCallback(CallbackInterface):
    def handle(self, message: EventSchema) -> bool:
        services = post_composer()
        return services.extract_posts(start_on=message.payload.get("start_on", 0))
