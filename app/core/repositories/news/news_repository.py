from ..base_repository import BaseRepository
from app.core.db import DBConnection
from app.core.entities import News, NewsInDB
from app.core.configs import get_logger
from typing import List

_logger = get_logger(__name__)


class NewsRepository(BaseRepository):
    def __init__(self, conn: DBConnection) -> None:
        super().__init__(conn)

    def insert(self, news: News) -> int:
        query = """
        INSERT
            INTO
            extract_news.news
        (title, link, description, author, inserted_at, created_at, updated_at)
        VALUES(%s, %s, %s, %s, %s, NOW(), NOW())
        RETURNING id;
        """
        try:
            self.connection.execute(
                sql_statement=query,
                values=(news.title, news.link, news.description, news.author, news.inserted_at),
            )

            result = self.connection.fetch()

            if result:
                return result["id"]

        except Exception as error:
            _logger.error(f"Some error happen on get_raw_response_by_id: {str(error)}")

    def get_all_news(self) -> List[NewsInDB]:
        query = """
        SELECT 
            *
        FROM extract_news.news
        WHERE link LIKE '%/negocios/%';
        """
        try:
            self.connection.execute(sql_statement=query)

            results = self.connection.fetch(all=True)

            news = []

            for result in results:
                news.append(NewsInDB(**result))

            return news

        except Exception as error:
            _logger.error(f"Some error happen on get_raw_response_by_id: {str(error)}")

