import json
from decimal import Decimal
from enum import Enum


class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Decimal):
            return f'{obj:.2f}'
        if isinstance(obj, Enum):
            return obj.value
        return super().default(obj)  # pragma: no cover
