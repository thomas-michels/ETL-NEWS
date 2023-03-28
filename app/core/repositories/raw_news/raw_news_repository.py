from app.core.entities import RawNews
import requests
from app.core.configs import get_environment, get_logger

_logger = get_logger(__name__)
_env = get_environment()


class RawNewsRepository:

    def get_news(self, link: str) -> RawNews:
        response = requests.request("GET", link)

        match response.status_code:
            case 200:
                json = response.json()

                raw_news = RawNews(link=link)
                raw_news.data["html"] = json["html"]

                return raw_news

            case _:
                _logger.error(
                    f"Some error happen on get_news - status_code: {response.status_code}"
                )

