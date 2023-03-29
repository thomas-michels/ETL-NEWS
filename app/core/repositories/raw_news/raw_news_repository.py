from app.core.entities import RawNews
import requests
from app.core.configs import get_logger
import time

_logger = get_logger(__name__)


class RawNewsRepository:

    def get_news(self, link: str) -> RawNews:
        response = requests.request("GET", link)
        time.sleep(1)

        match response.status_code:
            case 200:

                raw_news = RawNews(link=link)
                raw_news.data["html"] = response.text

                return raw_news

            case _:
                _logger.error(
                    f"Some error happen on get_news - status_code: {response.status_code}"
                )

