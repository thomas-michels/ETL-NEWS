from ..base_repository import BaseRepository
from app.core.entities import RawResponse
from app.core.db import DBConnection
from abc import abstractmethod
from typing import List


class RawResponseRepository(BaseRepository):

    def __init__(self, conn: DBConnection) -> None:
        super().__init__(conn)
    
    @abstractmethod
    def insert(self, raw_response: RawResponse) -> int:
        ...

    @abstractmethod
    def get_all_raw_response_ids(self) -> List[int]:
        ...

    @abstractmethod
    def get_raw_response_by_id(self, id: int) -> RawResponse:
        ...
