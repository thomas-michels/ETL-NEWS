from ..base_repository import BaseRepository
from app.core.entities import RawResponse
from app.core.db import DBConnection
from abc import abstractmethod


class RawResponseRepository(BaseRepository):

    def __init__(self, conn: DBConnection) -> None:
        super().__init__(conn)
    
    @abstractmethod
    def insert(self, raw_response: RawResponse) -> int:
        ...
