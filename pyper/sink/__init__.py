import typing as t
from enum import Enum

from google.cloud import bigquery
from pydantic import Field, BaseModel
from pydantic.main import BaseModel


class SinkStatus(str, Enum):
    NOT_STARTED = "not_started"
    STARTED = "started"
    ERROR = "error"
    DONE = "done"


class Sink(BaseModel):
    state: SinkStatus = Field(default=SinkStatus.NOT_STARTED)

    def execute(self) -> None:
        ...

    def update_state(self, state: SinkStatus):
        self.state = state


class SinkConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True
