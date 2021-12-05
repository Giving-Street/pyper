from typing import List, Any

from google.cloud import bigquery

from pyper import DataSource


class BigQuerySource(DataSource):
    client: bigquery.Client
    query: str

    def to_iterable(self) -> List[Any]:
        return self.__execute()

    def __execute(self) -> List[Any]:
        query_job = self.client.query(query=self.query)
        return list(query_job.result())
