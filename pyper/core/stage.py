from enum import Enum
from typing import List, Any, Callable, Union

from pydantic.fields import Field
from pydantic.main import BaseModel

from pyper.task import Task


class StageStatus(str, Enum):
    NOT_STARTED = "not_started"
    STARTED = "started"
    ERROR = "error"
    DONE = "done"


class Stage(BaseModel):
    result: List[Any] = Field(default_factory=list)
    status: StageStatus = StageStatus.NOT_STARTED
    task: Task = None
