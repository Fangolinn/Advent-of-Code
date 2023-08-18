import re
from pathlib import Path

INPUT_FILE = "input_ex.txt"
LIST_PATTERN = re.compile("\\[[^\\[\\]]*\\]")


def convert_line(line: str):
    converted = None

    while True:
        pass


if __name__ == "__main__":
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        while True:
            first_line = input_file.readline()
            second_line = input_file.readline()

            if not input_file.readline():
                break

            convert_line(first_line)
            convert_line(second_line)
