from app.core.db import DBConnection
from abc import ABC


class BaseRepository(ABC):
    def __init__(self, conn: DBConnection) -> None:
        self._conn = conn

    @property
    def connection(self) -> DBConnection:
        return self._conn
