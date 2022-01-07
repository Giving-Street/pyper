from enum import Enum
from typing import List, Any, Callable, Union, Optional

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
    status: StageStatus = Field(default=StageStatus.NOT_STARTED)
    last_task: Optional[Task] = Field(default=None)
    upstream: List["Stage"] = Field(default_factory=list)


Stage.update_forward_refs()
