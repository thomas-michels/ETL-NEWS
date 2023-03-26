"""
    Module for register queues
"""
from app.worker.consumer.manager import QueueManager
from app.core.configs import get_logger, get_environment
from app.worker.callbacks import ExtractCallback


_logger = get_logger(name=__name__)
_env = get_environment()


class RegisterQueues:
    """
    RegisterQueues class
    """

    @staticmethod
    def register() -> QueueManager:
        _logger.info("Starting QueueManager")
        queue_manager = QueueManager()

        queue_manager.register_callback(
            _env.EXTRACT_CHANNEL, ExtractCallback().handle
        )

        _logger.info("All queues started")

        return queue_manager
