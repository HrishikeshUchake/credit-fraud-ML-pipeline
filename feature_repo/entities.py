from feast import Entity, ValueType

# Define the user entity
user = Entity(
    name="user",
    join_keys=["user_id"],
    value_type=ValueType.INT64
)
