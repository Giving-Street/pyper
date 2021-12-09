from typing import List, Any

from pydantic.fields import Field
from pydantic.main import BaseModel


class Stage(BaseModel):
    result: List[Any] = Field(default_factory=list)

    def __eq__(self, other):
        if isinstance(other, Stage):
            return self.result == other.result
        return self.result == other
