from functools import lru_cache
from .environment import Environment
from .logger import Logger


@lru_cache()
def get_environment():
    return Environment()


@lru_cache()
def get_logger(name: str) -> Logger:
    return Logger(name=name).get_logger()
