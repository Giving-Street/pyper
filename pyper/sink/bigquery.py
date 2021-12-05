import json
import typing as t

from google.cloud import bigquery

from pyper import Sink, SinkConfig


class BigquerySinkConfig(SinkConfig):
    pass


class TargetTableNotFound(Exception):
    pass


class BigQuerySink(Sink):
    client: bigquery.Client
    config: BigquerySinkConfig

    def execute(self) -> None:
        if not self.config.is_streaming:
            raise NotImplemented()

        table_exists = self.client.get_table(table=self.config.target_table)
        if not table_exists:
            raise TargetTableNotFound()

        while True:
            entry = self._get_entry()
            self.client.insert_rows_json(table=self.config.target_table, json_rows=entry)

    def _get_entry(self) -> t.Sequence[dict]:
        return [json.dumps({"key": i}) for i in range(10)]  # TODO: get entry from shared state store

    class Config:
        arbitrary_types_allowed = True
