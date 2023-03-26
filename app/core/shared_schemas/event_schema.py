"""
    Module for event schemas
"""
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4


class EventSchema(BaseModel):
    """
    Event Schema
    """

    id: str = Field(default=uuid4())
    sended_to: str = Field(example="Extract")
    payload: dict = Field()
    creation_date: datetime = Field(default=datetime.now())
