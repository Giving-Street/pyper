from typing import Optional, List, Dict

from pyper.core import PipeAbstract
from pyper.core.stage import Stage, StageStatus
from pyper.sink import Sink
from pyper.source import DataSource
from pyper.task import Task


class Pipe(PipeAbstract):
    def __init__(self):
        self.source: Optional[DataSource] = None
        self.tasks: List[Task] = []
        self.sink: List[Sink] = []
        self.stages: Dict[Stage] = []

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
            try:
                stage.status = StageStatus.STARTED

                result = [task.fn(item) for item in stage.result]
                stage = Stage(result=result, status=StageStatus.DONE, task=task)
            except Exception as e:
                task.fallback(e)
                # TODO@grab: error handling type(rollback, maintain, ...)
                stage = Stage(result=[], status=StageStatus.ERROR, task=task)
                return stage
        return stage
