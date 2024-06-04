import pytest
from solve import duplicate_pair, is_nice_part1, is_nice_part2, same_with_one_between


@pytest.mark.parametrize("string", ["ugknbfddgicrmopn", "aaa"])
def test_is_nice_part1_positive(string: str) -> None:
    assert is_nice_part1(string)


@pytest.mark.parametrize(
    "string", ["jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
)
def test_is_nice_part1_negative(string: str) -> None:
    assert is_nice_part1(string) is False


@pytest.mark.parametrize("string", ["xyxy", "aabcdefgaa"])
def test_has_duplicate_pair_positive(string: str) -> None:
    assert duplicate_pair(string)


@pytest.mark.parametrize("string", ["aaa", "abcd", "ieodomkazucvgmuy"])
def test_has_duplicate_pair_negative(string: str) -> None:
    assert duplicate_pair(string) is False


@pytest.mark.parametrize("string", ["xyxy", "aaa", "abcdefeghi"])
def test_has_separated_two_positive(string: str) -> None:
    assert same_with_one_between(string)


@pytest.mark.parametrize("string", ["abc", "abcdb", "uurcxstgmygtbstg"])
def test_has_separated_two_negative(string: str) -> None:
    assert same_with_one_between(string) is False


@pytest.mark.parametrize("string", ["qjhvhtzxzqqjkmpb", "xxyxx"])
def test_is_nice_part2_positive(string: str) -> None:
    assert is_nice_part2(string)


@pytest.mark.parametrize("string", ["uurcxstgmygtbstg", "ieodomkazucvgmuy", "aaa"])
def test_is_nice_part2_negative(string: str) -> None:
    assert is_nice_part2(string) is False
