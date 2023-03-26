"""
    Module for callbacks interface
"""

from abc import abstractmethod, ABC
from app.core.shared_schemas import EventSchema


class CallbackInterface(ABC):
    """
    Class for callback base
    """

    @abstractmethod
    def handle(self, message: EventSchema) -> bool:
        """
        This method handle message and returns a bool

        :param:
            message
        :return: 
            Boolean
        """
