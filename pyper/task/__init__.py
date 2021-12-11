from typing import Any, Callable

from pydantic.main import BaseModel


class Task(BaseModel):
    fn: Callable[..., Any]
    fallback: Callable[[Exception], None] = lambda: None
