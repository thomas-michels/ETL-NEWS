"""
This module start connection with queues
"""

from app.worker.consumer import RegisterQueues
from app.core.configs import get_logger
from app.worker.consumer import KombuWorker
from app.worker.utils import start_connection_bus

_logger = get_logger(name=__name__)


class Worker:
    """This class start connection and worker"""

    def __init__(self) -> None:
        _logger.info("Creating Connection...")

        queues = RegisterQueues.register()
        self.start_consuming(queues)

    def start_consuming(self, queues):
        _logger.info("Start consuming...")
        try:
            with start_connection_bus() as conn:
                worker = KombuWorker(conn, queues)
                worker.run()

        except KeyboardInterrupt:
            _logger.info("Exiting...")
            quit()
