from typing import Optional, List

from pyper.core import PipeAbstract
from pyper.core.stage import Stage
from pyper.sink import Sink
from pyper.source import DataSource
from pyper.task import Task


class Pipe(PipeAbstract):
    def __init__(self):
        self.source: Optional[DataSource] = None
        self.tasks: List[Task] = []
        self.sink: List[Sink] = []

    def set_source(self, source: DataSource) -> "Pipe":
        self.source = source
        return self

    def add_task(self, task: Task) -> "Pipe":
        self.tasks.append(task)
        return self

    def add_sink(self, sink: Sink) -> "Pipe":
        self.sink.append(sink)
        return self

    # TODO@grab: fallback 로직 추가
    def run(self) -> Stage:
        _list = self.source.to_iterable()
        stage = Stage(result=_list)
        for task in self.tasks:
            stage = Stage(result=[task.fn(item) for item in stage.result])

        for sink in self.sink:
            sink.execute()  # TODO: execute in separate thread/process pool or async event loop

        return stage
