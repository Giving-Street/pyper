from typing import List, Any

from pydantic.fields import Field

from pyper import DataSource


class LocalSource(DataSource):
    data: List[Any] = Field(default_factory=[])

    def to_iterable(self):
        # Temp
        return self.data
