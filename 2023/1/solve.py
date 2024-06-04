import string
from pathlib import Path

from loguru import logger

INPUT_FILE = "input.txt"


def parse_input(input_file: str) -> list[str]:
    with open(Path(__file__).parent / input_file) as input:
        return [line.strip() for line in input.readlines()]


def extract_value(string: str) -> int:
    # combine first and last digit in string and return as int
    digits: list = [char for char in string if char.isdigit()]

    val = int(digits[0] + digits[-1])

    logger.info(f"Value extracted from {string}: {val}")

    return val


def part1() -> int:
    return sum([extract_value(data) for data in parse_input(INPUT_FILE)])


TEXT_TO_DIGITS: dict[str, str] = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_text_with_digits(data: str, map: dict[str, str] = TEXT_TO_DIGITS) -> str:
    # TODO could just replace one from the beginning, once from the end, overall can be improved
    logger.info(f"Before replace: {data}")

    while True:
        word: str | None = None
        index: int = len(data)

        for key in map:
            if key in data:
                current_key_index: int = data.index(key)
                if current_key_index < index:
                    logger.info(f"{current_key_index} < {index} ({key} < {word})")
                    index = current_key_index
                    word = key

        if word is not None:
            data = data.replace(word, map[word], 1)
            logger.info(f"Replace '{word}': {data}")
            continue

        break

    return data


def part2() -> int:
    return sum(
        [
            extract_value(replace_text_with_digits(data))
            for data in parse_input(INPUT_FILE)
        ]
    )


if __name__ == "__main__":
    print(part2())
