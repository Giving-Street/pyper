from typing import Any, Callable, Optional

from pydantic.fields import Field
from pydantic.main import BaseModel


class Task(BaseModel):
    fn: Callable[..., Any]
    fallback: Optional[Callable[[Exception], None]] = Field(default=None)
