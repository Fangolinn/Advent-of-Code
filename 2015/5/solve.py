# https://adventofcode.com/2015/day/5

from loguru import logger

VOWELS: str = "aeiou"


def at_least_three_vowels(string: str) -> bool:
    vowel_count = 0

    for c in string:
        if c in VOWELS:
            vowel_count += 1

        if vowel_count >= 3:
            return True

    return False


def two_in_a_row(string: str) -> bool:
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True

    return False


def no_forbidden_strings(
    string: str, forbidden_strings: list[str] = ["ab", "cd", "pq", "xy"]
) -> bool:
    for forbidden in forbidden_strings:
        if forbidden in string:
            return False

    return True


def is_nice_part1(string: str) -> bool:
    return (
        no_forbidden_strings(string)
        and at_least_three_vowels(string)
        and two_in_a_row(string)
    )


def duplicate_pair(string: str) -> bool:
    for i in range(len(string) - 3):
        if string[i : i + 2] in string[i + 2 :]:
            return True

    return False


def same_with_one_between(string: str) -> bool:
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


def is_nice_part2(string: str) -> bool:
    return duplicate_pair(string) and same_with_one_between(string)


if __name__ == "__main__":
    nice_strings = 0

    with open("input.txt") as input_file:
        for line in input_file.readlines():
            nice_strings += 1 if is_nice_part1(line) else 0

    print("Part 1: ", nice_strings)

    nice_strings = 0

    with open("input.txt") as input_file:
        for line in input_file.readlines():
            nice_strings += 1 if is_nice_part2(line) else 0

    print("Part 2: ", nice_strings)
