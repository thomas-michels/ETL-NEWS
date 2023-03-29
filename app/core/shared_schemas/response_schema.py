from pydantic import BaseModel, Field
from typing import List


class ResponseWithList(BaseModel):

    data: List[BaseModel] = Field()
