import abc

from pyper.sink import Sink
from pyper.source import DataSource
from pyper.core.stage import Stage
from pyper.task.base import Task


class PipeAbstract(abc.ABC):
    @abc.abstractmethod
    def set_source(self, source: DataSource) -> "PipeAbstract":
        raise NotImplemented("Not Implemented add_source method ")

    @abc.abstractmethod
    def add_task(self, task: Task) -> "PipeAbstract":
        pass

    @abc.abstractmethod
    def add_sink(self, sink: Sink) -> "PipeAbstract":
        pass

    @abc.abstractmethod
    def run(self) -> Stage:
        pass