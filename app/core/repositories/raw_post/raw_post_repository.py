import requests
from app.core.entities import RawResponse
from app.core.configs import get_environment, get_logger

_env = get_environment()
_logger = get_logger(__name__)


class RawPostRepository:
    def __init__(self) -> None:
        self.__params = {
            "page": "1",
            "order": "DESC",
            "scripts[0]": "jquery",
            "scripts[1]": "jquery-core",
            "query_args[pagename]": "ultimas-noticias",
            "query_args[post_type][0]": "guide",
            "query_args[post_type][1]": "post",
            "query_args[posts_per_page]": "10",
            "query_args[post_type][2]": "page",
            "query_args[post_type][3]": "colunistas",
            "query_args[post_type][4]": "patrocinados",
            "query_args[post_type][5]": "especiais",
            "query_args[post_type][6]": "web-story",
        }

    def get_raw_posts(self, page: int, page_size: int) -> RawResponse:
        self.__params["page"] = str(page)
        self.__params["query_args[posts_per_page]"] = str(page_size)

        response = requests.request("POST", _env.RAW_POSTS_URL, data=self.__params)

        match response.status_code:
            case 200:
                json = response.json()

                raw_response = RawResponse()
                raw_response.data["html"] = json["html"]

                return raw_response

            case _:
                _logger.error(
                    f"Some error happen on get_raw_posts - status_code: {response.status_code}"
                )
