from .raw_response_repository import RawResponseRepository
from app.core.db import DBConnection
from app.core.entities import RawResponse
from app.core.configs import get_logger
from json import dumps
from typing import List

_logger = get_logger(__name__)


class PGRawResponseRepository(RawResponseRepository):

    def __init__(self, conn: DBConnection) -> None:
        super().__init__(conn)

    def insert(self, raw_response: RawResponse) -> int:
        query = """
        INSERT
            INTO
            extract_news.raw_response
        ("data",
            created_at,
            updated_at)
        VALUES(%s, NOW(), NOW())
        RETURNING id;
        """
        try:
            self.connection.execute(sql_statement=query, values=(dumps(raw_response.data),))

            result = self.connection.fetch()

            if result:
                return result["id"]
            
        except Exception as error:
            _logger.error(f"Some error happen on insert raw response: {str(error)}")

    def get_raw_response_by_id(self, id: int) -> RawResponse:
        query = """
        SELECT
            id,
            "data",
            created_at,
            updated_at
        FROM
            extract_news.raw_response
        WHERE id=%s;
        """
        try:
            self.connection.execute(sql_statement=query, values=(id,))

            result = self.connection.fetch()

            if result:
                return RawResponse(**result)
            
        except Exception as error:
            _logger.error(f"Some error happen on get_raw_response_by_id: {str(error)}")

    
    def get_all_raw_response_ids(self) -> List[int]:
        query = """
        SELECT
            array_agg(id) AS ids
        FROM
            extract_news.raw_response;
        """
        try:
            self.connection.execute(sql_statement=query)

            result = self.connection.fetch()

            if result:
                return result["ids"]
            
        except Exception as error:
            _logger.error(f"Some error happen on get_all_raw_response_ids: {str(error)}")
