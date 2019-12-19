import json
from decimal import Decimal
from enum import Enum

import pytest

from {{cookiecutter.project_slug}}.contrib.json import JSONEncoder


class _SimpleEnum(Enum):
    VALUE = 'value'


class TestJSONEncoder:

    @pytest.mark.parametrize('data,expected', (
        ({'s': 'simple'}, '{"s": "simple"}'),
        ({'i': 1}, '{"i": 1}'),
        ({'f': 1.2}, '{"f": 1.2}'),
        ({'b': True}, '{"b": true}'),
        ({'n': None}, '{"n": null}'),
        ({'d': Decimal('10.00')}, '{"d": "10.00"}'),
        ({'e': _SimpleEnum.VALUE}, '{"e": "value"}'),
    ))
    def test_should_encode_decimal_and_native_types(self, data, expected):
        assert json.dumps(data, cls=JSONEncoder) == expected
