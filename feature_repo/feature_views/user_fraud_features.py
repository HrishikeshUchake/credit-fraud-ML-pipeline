from feast import FeatureView, Field
from feast.value_type import ValueType
from datetime import timedelta

from entities import card_entity
from data_sources.transactions import transactions_source
user_fraud_features = FeatureView(
    name="user_fraud_features",
    entities=[card_entity],                  # list of Entity objects
    ttl=timedelta(days=1),
    online=True,
    source=transactions_source,              # <— note “source=”
    schema=[
        Field(name="Amount", dtype=ValueType.FLOAT),
        Field(name="Class",  dtype=ValueType.INT64),
    ],
    tags={"team": "fraud-detection"},
)
