import json
import typing as t

import pytest
from tinyquery import tinyquery

from pyper.source.bigquery import BigQuerySource


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
    client.load_table_from_newline_delimited_json("test_data", schema=json.dumps(bigquery_test_data_schema["fields"]),
                                                  table_lines=[json.dumps({"name": f"test-{i + 1}", "value": i + 1}) for
                                                               i in
                                                               range(100)])
    return client


class FakeBigQuerySource(BigQuerySource):
    def to_iterable(self) -> t.List[t.Any]:
        return self.__execute()

    def __execute(self) -> t.List[t.Any]:
        return self.client.evaluate_query(self.query).columns[(None, 'value')].values