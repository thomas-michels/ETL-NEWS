from pydantic.generics import GenericModel
from pydantic import Field
from datetime import datetime


class Post(GenericModel):
    title: str = Field(example="post")
    link: str = Field(example="www.url.com")


class PostInDB(Post):
    id: int = Field(example=123)
    created_at: datetime = Field(example=str(datetime.now()))
    updated_at: datetime = Field(example=str(datetime.now()))
