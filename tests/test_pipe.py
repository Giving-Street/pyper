from pyper.core.pipe import Pipe
from pyper.core.stage import StageStatus, Stage
from pyper.source.local import LocalSource
from pyper.task.map import MapTask


def test_pipe_initialized():
    nums = [1, 2, 3, 4]
    fn = lambda x: x * 2
    pipe = Pipe()
    map_task1 = MapTask(fn=fn)
    map_task2 = MapTask(fn=fn)

    stage = (
        pipe.set_source(LocalSource(data=nums))
        .add_task(map_task1)
        .add_task(map_task2)
        .run()
    )

    assert stage == Stage(
        result=[fn(fn(num)) for num in nums], task=map_task2, status=StageStatus.DONE
    )


def test_pipe_exception_occurred(capsys):
    nums = [1, 2, 3, 4]
    except_task = MapTask(
        fn=lambda x: exec('raise(Exception("error"))'), fallback=lambda x: print(x)
    )
    map_task = MapTask(fn=lambda x: x * 2)
    pipe = Pipe()

    stage = (
        pipe.set_source(LocalSource(data=nums))
        .add_task(except_task)
        .add_task(map_task)
        .run()
    )

    assert stage == Stage(result=[], task=except_task, status=StageStatus.ERROR)

    captured = capsys.readouterr()
    assert captured.out == "error\n"
