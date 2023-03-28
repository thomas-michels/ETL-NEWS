from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Dict


class RawNews(BaseModel):
    title: str = Field(example="post", default="")
    link: HttpUrl = Field(example="www.url.com")
    data: Dict[str, str | int] = Field(default={})


class RawNewsInDB(RawNews):
    id: int = Field(example=123)
    created_at: datetime = Field(example=str(datetime.now()))
    updated_at: datetime = Field(example=str(datetime.now()))
