from app.core.repositories.raw_news import RawNewsRepository
from app.core.repositories.raw_response import RawResponseRepository
from app.core.repositories.post import PostRepository
from app.core.entities import Post
from app.worker.producer import KombuProducer
from app.core.configs import get_logger, get_environment
from app.worker.utils import payload_conversor
from bs4 import BeautifulSoup
import re
import time

_logger = get_logger(__name__)
_env = get_environment()


class NewsServices:
    def __init__(
        self,
        raw_response_repository: RawResponseRepository,
        rawnews_repository: RawNewsRepository,
        post_repository: PostRepository
    ) -> None:
        self.__raw_response_repository = raw_response_repository
        self.__news_repository = news_repository
        self.__post_repository = post_repository
