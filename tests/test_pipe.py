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

    assert stage.result == [fn(fn(num)) for num in nums]
    assert stage.status == StageStatus.DONE
    assert stage.task == map_task2


def test_pipe_exception_occurred(capsys):
    nums = [1, 2, 3, 4]

    def except_occurred(_):
        raise Exception("error")

    except_task = MapTask(fn=except_occurred, fallback=lambda x: print(x))
    map_task = MapTask(fn=lambda x: x * 2)
    pipe = Pipe()

    stage = (
        pipe.set_source(LocalSource(data=nums))
        .add_task(except_task)
        .add_task(map_task)
        .run()
    )

    assert stage.status == StageStatus.ERROR
    assert stage.result == []
    assert stage.task == except_task

    captured = capsys.readouterr()
    assert captured.out == "error\n"
