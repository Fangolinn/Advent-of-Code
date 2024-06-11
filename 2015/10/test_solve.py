import pytest
from solve import look_and_say


@pytest.mark.parametrize(
    "iterations, expected_sequence",
    [(1, "11"), (2, "21"), (3, "1211"), (4, "111221"), (5, "312211")],
)
def test_look_and_say(iterations: int, expected_sequence: str) -> None:
    assert look_and_say("1", iterations) == expected_sequence
