import abc
from typing import List, Any

from pydantic.main import BaseModel


class DataSource(abc.ABC, BaseModel):
    @abc.abstractmethod
    def to_iterable(self) -> List[Any]:
        pass
