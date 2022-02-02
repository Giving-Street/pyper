from typing import Callable, Any

from pydantic import BaseModel


class Task(BaseModel):
    fn: Callable[..., Any]