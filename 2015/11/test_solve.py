from string import ascii_lowercase

import pytest
from solve import (
    find_new_password,
    increment_string,
    is_password_valid,
    is_valid_rule_contains_straight_of_letters,
    is_valid_rule_contains_two_pairs,
    is_valid_rule_no_forbidden_letters,
)


@pytest.mark.parametrize(
    "password, is_valid", [("abc", True), ("abd", False), ("hijklmmn", True)]
)
def test_rule_check_contains_straight_of_letters(password: str, is_valid: bool) -> None:
    assert is_valid_rule_contains_straight_of_letters(password) is is_valid


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("i", False),
        ("o", False),
        ("l", False),
        (ascii_lowercase.translate(dict.fromkeys(map(ord, "iol"), None)), True),
    ],
)
def test_rule_check_does_not_contain_forbidden_letters(
    password: str, is_valid: bool
) -> None:
    assert is_valid_rule_no_forbidden_letters(password) is is_valid


@pytest.mark.parametrize(
    "password, is_valid", [("a", False), ("aaa", False), ("aaaa", True)]
)
def test_rule_check_contains_two_separate_pairs(password: str, is_valid: bool) -> None:
    assert is_valid_rule_contains_two_pairs(password) is is_valid


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("hijklmmn", False),
        ("abbceffg", False),
        ("abbcegjk", False),
        ("abcdffaa", True),
        ("ghjaabcc", True),
    ],
)
def test_is_valid(password: str, is_valid: bool) -> None:
    assert is_password_valid(password) is is_valid


@pytest.mark.parametrize(
    "current, expected_next",
    [("xx", "xy"), ("xy", "xz"), ("xz", "ya"), ("ya", "yb"), ("z", "aa")],
)
def test_increment_string(current: str, expected_next: str) -> None:
    assert increment_string(current) == expected_next


@pytest.mark.parametrize(
    "original, expected_new_password",
    [("abcdefgh", "abcdffaa"), ("ghijklmn", "ghjaabcc"), ("a", "aabcc")],
)
def test_find_new_password(original: str, expected_new_password: str) -> None:
    assert find_new_password(original) == expected_new_password
