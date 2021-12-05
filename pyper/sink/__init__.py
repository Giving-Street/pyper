from enum import Enum

from pydantic import Field
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
