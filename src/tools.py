from decimal import Decimal
from typing import Dict, Any

from google.protobuf.message import Message
from google.protobuf.pyext._message import RepeatedCompositeContainer, MessageMapContainer
from google.protobuf.timestamp_pb2 import Timestamp


def message_to_dict(message_table: Message, set_default_values: bool = True) -> Dict[str, Any]:
    """
    The function is not tested to work with fields of google.protobuf.Struct etc.
    Function converts 'amount' field_descriptor from string to Decimal and Timestamp fields
    to datetime.
    """

    def pythonify_value(field_name: str, field_value: Any) -> Any:
        if isinstance(field_value, Timestamp):
            return field_value.ToDatetime()
        if isinstance(field_value, str) and field_name == 'amount':
            return Decimal(field_value)

        return field_value

    def get_actual_field_value(field_name: str) -> Any:
        for field_descriptor, field_value in message_table.ListFields():
            if field_descriptor.name == field_name:
                if isinstance(field_value, RepeatedCompositeContainer):
                    return [message_to_dict(f) for f in field_value]
                if isinstance(field_value, MessageMapContainer):
                    return {k: message_to_dict(field_value[k]) for k in field_value}

                return pythonify_value(field_name, field_value)

        return None

    result = {}
    if len(message_table.DESCRIPTOR.oneofs_by_name.items()):
        result['which_oneof'] = {}
        for k, v in message_table.DESCRIPTOR.oneofs_by_name.items():
            result['which_oneof'][k] = message_table.WhichOneof(k)

    for field_name, field_descriptor in message_table.DESCRIPTOR.fields_by_name.items():
        value = get_actual_field_value(field_name)

        if value is None:
            if not set_default_values:
                continue

            # @TODO How to handle the map type to set default value to the dict instead of the list?
            value = field_descriptor.default_value

        result[field_name] = value

    return result
