from pyper.core.pipe import Pipe
from pyper.source.local import LocalSource
from pyper.task.map import MapTask
from tests.conftest import FakeBigQuerySource


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


def test_pipe_bigquery_source(bigquery_test_client):
    fn = lambda x: x * 2
    expected = [4, 8, 12, 16]

    stage = Pipe() \
        .set_source(FakeBigQuerySource(client=bigquery_test_client, query="select value from test_data limit 4")) \
        .add_task(MapTask(fn=fn)) \
        .add_task(MapTask(fn=fn)) \
        .run()

    assert stage.result == expected
