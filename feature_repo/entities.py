from feast import Entity
from feast.value_type import ValueType

card_entity = Entity(
    name="card_id",                          # the logical “join key”
    value_type=ValueType.STRING,             # match the type in your CSV
    description="Credit-card identifier"
)
