from abc import abstractmethod
from enum import Enum

from pydantic import BaseModel, Field


class SinkStatus(str, Enum):
    NOT_STARTED = "not_started"
    STARTED = "started"
    ERROR = "error"
    DONE = "done"


class Sink(BaseModel):
    state: SinkStatus = Field(default=SinkStatus.NOT_STARTED)

    @abstractmethod
    def execute(self) -> None:
        pass

    def update_state(self, state: SinkStatus):
        self.state = state


class SinkConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True