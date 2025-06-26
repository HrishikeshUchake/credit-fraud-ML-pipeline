from feast import FileSource
from feast.types import DataFormat   # if you really want the enum

transactions_source = FileSource(
    path="data/transactions.csv",
    event_timestamp_column="event_timestamp",
    file_format="csv"               # or DataFormat.CSV
)
