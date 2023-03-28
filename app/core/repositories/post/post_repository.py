from ..base_repository import BaseRepository
from app.core.db import DBConnection
from app.core.entities import Post
from app.core.configs import get_logger, get_environment

_logger = get_logger(__name__)
_env = get_environment()


class PostRepository(BaseRepository):
    def __init__(self, conn: DBConnection) -> None:
        super().__init__(conn)

    def insert(self, post: Post) -> int:
        query = """
        INSERT
            INTO
            extract_news.post
            (title,
            link,
            created_at,
            updated_at)
        VALUES(%s, %s, NOW(), NOW())
        RETURNING id;
        """
        try:
            self.connection.execute(sql_statement=query, values=(post.title, post.link))

            result = self.connection.fetch()

            if result:
                return result["id"]

        except Exception as error:
            _logger.error(f"Some error happen on get_raw_response_by_id: {str(error)}")
