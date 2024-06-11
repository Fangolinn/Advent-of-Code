import pytest
from solve import count_chars_in_memory, encoded_len


@pytest.mark.parametrize(
    "string, expected_count", [("", 0), ("abc", 3), ('aaa\\"aaa', 7), ("\x27", 1)]
)
def test_count_chars_in_memory(string: str, expected_count: int) -> None:
    assert count_chars_in_memory(string) == expected_count


@pytest.mark.parametrize(
    "string, expected_len",
    [('""', 6), ('"abc"', 9), ('"aaa\\"aaa"', 16), ('"\x27"', 11)],
)
def test_get_encoded_length(string: str, expected_len: int):
    assert encoded_len(string) == expected_len
