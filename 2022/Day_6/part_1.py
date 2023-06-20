# https://adventofcode.com/2022/day/6

# + part 2

from pathlib import Path

MARKER_SIZE = 14

def main():
    with open(Path(__file__).parent / "input.txt") as input_file:
        line = input_file.readline()
        buffer = []

        for c, i in zip(line, range(len(line))):
            if len(set(buffer) | {c}) == MARKER_SIZE:
                return i + 1

            buffer.append(c)

            if len(buffer) == MARKER_SIZE:
                buffer.pop(0)


if __name__ == "__main__":
    print(main())
