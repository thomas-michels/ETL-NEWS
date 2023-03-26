"""
Kombu worker class module
"""

from kombu.mixins import ConsumerMixin
from app.core.configs import get_logger
from app.worker.consumer.manager import QueueManager
from app.worker.utils import payload_conversor

_logger = get_logger(name=__name__)


class KombuWorker(ConsumerMixin):
    """
    This class is Kombu Worker
    """

    def __init__(self, connection, queues: QueueManager):
        self.queues = queues
        self.connection = connection

    def get_consumers(self, consumer, channel):
        return [
            consumer(queues=self.queues.get_queues(), callbacks=[self.process_task])
        ]

    def process_task(self, body, message):
        try:
            infos = message.delivery_info
            _logger.info(f"Message received at {infos['routing_key']}")
            function = self.queues.get_function(infos["routing_key"])
            event_schema = payload_conversor(body)
            if event_schema:
                if function(event_schema):
                    message.ack()

        except Exception as error:
            _logger.error(f"Error on process_task - {error}")
