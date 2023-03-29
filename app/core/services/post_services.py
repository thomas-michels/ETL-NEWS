from app.core.repositories.raw_post import RawPostRepository
from app.core.repositories.raw_response import RawResponseRepository
from app.core.repositories.post import PostRepository
from app.core.entities import Post
from app.worker.producer import KombuProducer
from app.core.configs import get_logger, get_environment
from app.worker.utils import payload_conversor
from bs4 import BeautifulSoup
import re
import time

_TITLE_REGEX = r'<a href="(.+?)"\s+title="(.+?)">'
_logger = get_logger(__name__)
_env = get_environment()


class PostServices:
    def __init__(
        self,
        raw_response_repository: RawResponseRepository,
        raw_post_repository: RawPostRepository,
        post_repository: PostRepository,
    ) -> None:
        self.__raw_response_repository = raw_response_repository
        self.__raw_post_repository = raw_post_repository
        self.__post_repository = post_repository

    def start_extract(self, start_page: int = 0) -> bool:
        start = max(1, start_page)

        _logger.info(f"Extracting {_env.BATCH_SIZE * 100} posts")

        fail_count = 0
        for page in range(start, _env.BATCH_SIZE):
            _logger.info(f"Extract progress - {page}/{_env.BATCH_SIZE}")
            if fail_count > 3:
                _logger.error(f"Stopping batch - page: {page}")
                return False

            raw_response = self.__raw_post_repository.get_raw_posts(
                page=page, page_size=_env.BATCH_SIZE
            )

            if raw_response:
                saved = self.__raw_response_repository.insert(raw_response=raw_response)
                if not saved:
                    _logger.error(f"raw_response not saved: {raw_response.dict()}")

                self.__raw_response_repository.connection.commit()

            else:
                fail_count += 1

            time.sleep(1)

        if page < (_env.BATCH_SIZE - 1):
            message = payload_conversor(
                raw_payload={
                    "sended_to": _env.EXTRACT_CHANNEL,
                    "payload": {"start": page},
                }
            )
            producer = KombuProducer()
            producer.send_messages(message=message)
            _logger.info(f"Start stopped on {page}")

        else:
            message = payload_conversor(
                raw_payload={
                    "sended_to": _env.EXTRACT_POST_CHANNEL,
                    "payload": {},
                }
            )

            producer = KombuProducer()
            producer.send_messages(message=message)
            _logger.info(f"Extract completed!")

        return True

    def extract_posts(self, start_on: int = 0) -> bool:
        ids = self.__raw_response_repository.get_all_raw_response_ids()

        if start_on != 0:
            start_on = ids.index(start_on)

        try:
            for index, id in enumerate(ids, start_on):
                raw_response = self.__raw_response_repository.get_raw_response_by_id(
                    id=id
                )

                if raw_response:
                    soup = BeautifulSoup(raw_response.data["html"], "html.parser")

                    posts = soup.find_all("div", class_="row py-3 item")

                    for post in posts:
                        sub_item = str(post.find("a"))

                        match = re.search(_TITLE_REGEX, sub_item)

                        if match:
                            link = match.group(1)
                            title = match.group(2)

                            post_entity = Post(title=title, link=link)

                            post_id = self.__post_repository.insert(post_entity)
                            self.__post_repository.connection.commit()
                            _logger.info(
                                f"New post - title: {post_entity.title}, url: {post_entity.link}"
                            )

                            message = payload_conversor(
                                raw_payload={
                                    "sended_to": _env.EXTRACT_NEWS_CHANNEL,
                                    "payload": {"post_id": post_id},
                                }
                            )
                            producer = KombuProducer()
                            producer.send_messages(message=message)

                else:
                    _logger.warning(f"Raw response with id {id} not found")

            _logger.info(f"Extract post completed!")
            return True

        except Exception as error:
            _logger.error(f"Some error happen on extract posts: {str(error)}")
            _logger.info(f"Last raw_response id consumed is {id}")

            message = payload_conversor(
                raw_payload={
                    "sended_to": _env.EXTRACT_POST_CHANNEL,
                    "payload": {"start_on": id},
                }
            )
            producer = KombuProducer()
            producer.send_messages(message=message)

            return True
