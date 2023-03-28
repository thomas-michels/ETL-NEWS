from .callback_base import CallbackInterface
from app.core.shared_schemas import EventSchema
from app.core.composer import news_composer
from app.core.configs import get_logger

_logger = get_logger(__name__)


class ExtractRawNewsCallback(CallbackInterface):
    def handle(self, message: EventSchema) -> bool:
        services = news_composer()

        result = services.extract_raw_news(post_id=message.payload["post_id"])

        if result:
            _logger.info(
                f"New news inseted from post_id: {message.payload['post_id']}!"
            )
            return True

        _logger.error(f"News not inserted from post_id: {message.payload['post_id']}!")
