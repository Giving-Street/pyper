from pyper.core.pipe import Pipe
from pyper.source.local import LocalSource
from pyper.task.map import MapTask


def test_pipe_initialized():
    nums = [1, 2, 3, 4]
    fn = lambda x: x * 2
    pipe = Pipe()
    expected = [4, 8, 12, 16]

    stage = (
        pipe.set_source(LocalSource(data=nums))
        .add_task(MapTask(fn=fn))
        .add_task(MapTask(fn=fn))
        .run()
    )

    assert stage == expected
