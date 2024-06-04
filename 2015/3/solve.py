from collections import namedtuple
from pathlib import Path

INPUT_FILE = "input.txt"

Point = namedtuple("Point", ["x", "y"])


def move(direction: str, current_pos: Point) -> Point:
    match direction:
        case "^":
            return Point(current_pos.x, current_pos.y + 1)
        case ">":
            return Point(current_pos.x + 1, current_pos.y)
        case "v":
            return Point(current_pos.x, current_pos.y - 1)
        case "<":
            return Point(current_pos.x - 1, current_pos.y)
        case _:
            raise ValueError(f"Unknown direction {direction}")


def part1(path: str) -> int:
    visited: set[Point] = set()
    current_pos = Point(0, 0)

    for direction in path:
        visited.add(current_pos)
        current_pos = move(direction, current_pos)

    return len(visited)


def part2(path: str) -> int:
    visited: set[Point] = set()

    # real
    current_pos = Point(0, 0)
    for direction in path[::2]:
        visited.add(current_pos)
        current_pos = move(direction, current_pos)

    visited.add(current_pos)

    # robo
    current_pos = Point(0, 0)
    for direction in path[1::2]:
        visited.add(current_pos)
        current_pos = move(direction, current_pos)

    visited.add(current_pos)

    return len(visited)


if __name__ == "__main__":
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        path: str = input_file.readline()

    print(part2(path))
