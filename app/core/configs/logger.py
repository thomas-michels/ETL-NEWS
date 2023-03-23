"""
Looger Module
"""
import logging


class Logger:
    """
    Logger class
    """

    INFO = logging.INFO
    DEBUG = logging.DEBUG
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITITAL = logging.CRITICAL

    def __init__(self, name=__name__):
        self.logger_worker = logging.getLogger(name)
        self.__config_logger()

    def __config_logger(self):
        self.logger_worker.setLevel(self.DEBUG)
        self.__config_handler(logging.DEBUG)
        self.__config_handler(logging.DEBUG, "debug.log")

    def __config_handler(self, level, file=None):
        console_handler = logging.FileHandler(file) if file else logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter(
            "%(levelname)s\t| %(asctime)s| %(module)s:%(lineno)s => %(message)s\t"
        )
        console_handler.setFormatter(formatter)
        self.logger_worker.addHandler(console_handler)

    def get_logger(self):

        return self.logger_worker
