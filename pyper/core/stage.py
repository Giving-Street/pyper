from typing import List, Any

from pydantic.fields import Field
from pydantic.main import BaseModel


class Stage(BaseModel):
    result: List[Any] = Field(default_factory=[])
