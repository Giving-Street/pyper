import json
import typing as t

import pytest
from google.cloud.bigquery import TableReference, DatasetReference
from pydantic import Field
from tinyquery import tinyquery

from pyper import SinkStatus, BigQuerySink, BigquerySinkConfig, BigQuerySource


@pytest.fixture
def bigquery_test_data_schema():
    return {
        "fields": [
            {
                'name': 'name',
                'type': 'STRING',
                'mode': 'NULLABLE',
            },
            {
                'name': 'value',
                'type': 'INTEGER',
                'mode': 'NULLABLE',
            },
        ]
    }


@pytest.fixture
def bigquery_test_client(bigquery_test_data_schema):
    client = tinyquery.TinyQuery()
    client.load_table_from_newline_delimited_json("test.test_data",
                                                  schema=json.dumps(bigquery_test_data_schema["fields"]),
                                                  table_lines=[json.dumps({"name": f"test-{i + 1}", "value": i + 1}) for
                                                               i in
                                                               range(100)])
    client.make_empty_table("test.test_target_data", bigquery_test_data_schema)
    return client


class FakeBigQuerySource(BigQuerySource):
    client: tinyquery.TinyQuery

    def to_iterable(self) -> t.List[t.Any]:
        return self.__execute()

    def __execute(self) -> t.List[t.Any]:
        return self.client.evaluate_query(self.query).columns[(None, 'value')].values


class FakeBigQuerySink(BigQuerySink):
    client: tinyquery.TinyQuery
    schema_: t.Dict[str, t.Any] = Field(alias="schema")
    config: BigquerySinkConfig = Field(
        default=BigquerySinkConfig(
            target_table=TableReference(dataset_ref=DatasetReference("", "test"), table_id="test_target_data")))

    def execute(self) -> None:
        entry = self._get_entry()
        table_lines = [json.dumps(item) for item in entry]
        self.client.load_table_from_newline_delimited_json(table_name=self.config.target_table, table_lines=table_lines,
                                                           schema=json.dumps(self.schema_["fields"]))
        self.update_state(state=SinkStatus.DONE)

    def _get_entry(self) -> t.Sequence[dict]:
        return [{"name": "test", "value": i} for i in range(10)] # TODO: get from shared state
