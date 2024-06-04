import pytest
from solve import extract_value, replace_text_with_digits


@pytest.mark.parametrize(
    "string, expected",
    [
        ("1", 11),
        ("12", 12),
        ("123", 13),
        ("1234", 14),
        ("12345", 15),
        ("123456", 16),
        ("1234567", 17),
        ("12345678", 18),
        ("123456789", 19),
        ("1234567890", 10),
        ("7", 77),
        ("jmgpmfx2hvxsfr372", 22),
    ],
)
def test_extract_value(string: str, expected: int) -> None:
    assert extract_value(string) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("one", "1"),
        ("one two", "1 2"),
        ("one two three", "1 2 3"),
        ("one two three four", "1 2 3 4"),
        ("one two three four five", "1 2 3 4 5"),
        ("one two three four five six", "1 2 3 4 5 6"),
        ("one two three four five six seven", "1 2 3 4 5 6 7"),
        ("one two three four five six seven eight", "1 2 3 4 5 6 7 8"),
        ("one two three four five six seven eight nine", "1 2 3 4 5 6 7 8 9"),
        ("threetwonefour", "32ne4"),
        ("jmgpmfxtwohvxsfr3seventwo", "jmgpmfx2hvxsfr372"),
    ],
)
def test_convert_text(input: str, expected: str) -> None:
    assert replace_text_with_digits(input) == expected
