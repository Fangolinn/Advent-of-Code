import json

import pytest
from solve import sum_with_python, sum_with_python_part2

TEST_DATA: list[tuple[str, int]] = [
    ("[1,2,3]", 6),
    ('{"a":2,"b":4}', 6),
    ("[[[3]]]", 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ("[]", 0),
    ("{}", 0),
]


@pytest.mark.parametrize("data, expected_sum", TEST_DATA)
def test_sum_with_python(data: str, expected_sum: int) -> None:
    assert sum_with_python(json.loads(data)) == expected_sum


TEST_DATA_PART_2: list[tuple[str, int]] = [
    ("[1,2,3]", 6),
    ('[1,{"c":"red","b":2},3]', 4),
    ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
    ('[1,"red",5]', 6),
    ("[]", 0),
    ("{}", 0),
]


@pytest.mark.parametrize("data, expected_sum", TEST_DATA_PART_2)
def test_sum_with_python_part2(data: str, expected_sum: int):
    assert sum_with_python_part2(json.loads(data)) == expected_sum
