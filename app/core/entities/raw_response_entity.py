from pydantic.generics import GenericModel
from pydantic import Field
from typing import Dict
from datetime import datetime


class RawResponse(GenericModel):
    data: Dict[str, str | int] = Field(default={})


class RawResponseInDB(RawResponse):
    id: int = Field(example=123)
    created_at: datetime = Field(example=str(datetime.now()))
    updated_at: datetime = Field(example=str(datetime.now()))
