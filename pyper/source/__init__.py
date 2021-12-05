import abc
from typing import List, Any

from pydantic.main import BaseModel


class DataSource(BaseModel):
    @abc.abstractmethod
    def to_iterable(self) -> List[Any]:
        pass

    class Config:
        arbitrary_types_allowed = True
        allow_mutation = True
        underscore_attrs_are_private = True
