from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime


class News(BaseModel):
    title: str = Field(example="post")
    description: str = Field(example="post")
    link: HttpUrl = Field(example="www.url.com")
    author: str = Field(example="post")
    inserted_at: datetime = Field(example=str(datetime.now()))


class NewsInDB(News):
    id: int = Field(example=123)
    created_at: datetime = Field(example=str(datetime.now()))
    updated_at: datetime = Field(example=str(datetime.now()))
