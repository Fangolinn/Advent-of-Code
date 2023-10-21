from collections import namedtuple
from pathlib import Path

INPUT_FILE = "input.txt"

Point = namedtuple("Point", "x, y")

SOLID_POINTS: set[Point] = set()
SAND_ENTRY: Point = Point(500, 0)


def parse_points(line: str) -> list[Point]:
    line_split = line.strip("\n").split(" -> ")

    points = []
    for point in line_split:
        point = point.split(",")
        points.append(Point(int(point[0]), int(point[1])))

    return points


def add_line(start_point: Point, end_point: Point) -> None:
    SOLID_POINTS.add(start_point)

    if start_point.x == end_point.x:
        if end_point.y > start_point.y:
            y = start_point.y + 1

            while end_point.y > y:
                SOLID_POINTS.add(Point(start_point.x, y))
                y += 1

        if end_point.y < start_point.y:
            y = start_point.y - 1

            while end_point.y < y:
                SOLID_POINTS.add(Point(start_point.x, y))
                y -= 1

    if start_point.y == end_point.y:
        if end_point.x > start_point.x:
            x = start_point.x + 1

            while end_point.x > x:
                SOLID_POINTS.add(Point(x, start_point.y))
                x += 1

        if end_point.x < start_point.x:
            x = start_point.x - 1

            while end_point.x < x:
                SOLID_POINTS.add(Point(x, start_point.y))
                x -= 1

    SOLID_POINTS.add(end_point)


def determine_path(points: list[Point]) -> None:
    for start, end in zip(points[:-1], points[1:]):
        add_line(start, end)


def check_move(grain: Point = SAND_ENTRY) -> Point:
    if Point(grain.x, grain.y + 1) not in SOLID_POINTS:
        return Point(grain.x, grain.y + 1)

    if Point(grain.x - 1, grain.y + 1) not in SOLID_POINTS:
        return Point(grain.x - 1, grain.y + 1)

    if Point(grain.x + 1, grain.y + 1) not in SOLID_POINTS:
        return Point(grain.x + 1, grain.y + 1)

    return grain


# Part 1
def main01() -> None:
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        for line in input_file.readlines():
            determine_path(parse_points(line))

    max_y = max([point.y for point in SOLID_POINTS])
    grains_count: int = 0

    while True:
        # print(f"Grain {grains_count}")
        grain = SAND_ENTRY

        while True:
            prev_position = grain
            grain = check_move(grain)

            if grain == prev_position:
                SOLID_POINTS.add(grain)
                break

            # Check if grain is falling into the void
            if grain.y >= max_y:
                break

        if grain == SAND_ENTRY:
            break

        # Check if grain is falling into the void
        if grain.y >= max_y:
            break

        grains_count += 1

    print("Out:", grains_count)


# Part 2
def main02() -> None:
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        for line in input_file.readlines():
            determine_path(parse_points(line))

    floor = max([point.y for point in SOLID_POINTS]) + 2
    grains_count: int = 0

    while True:
        # print(f"Grain {grains_count}")
        grain = SAND_ENTRY

        while True:
            prev_position = grain
            grain = check_move(grain)

            if grain == prev_position:
                SOLID_POINTS.add(grain)
                break

            # Check if grain is falling into the void
            if grain.y >= floor - 1:
                SOLID_POINTS.add(grain)
                break

        grains_count += 1

        if grain == SAND_ENTRY:
            break

    print("Out:", grains_count)


def print_scan() -> None:
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        for line in input_file.readlines():
            determine_path(parse_points(line))

    start_col = min([point.x for point in SOLID_POINTS])
    end_col = max([point.x for point in SOLID_POINTS])
    floor = max([point.y for point in SOLID_POINTS]) + 2

    for y in range(floor):
        for x in range(start_col, end_col + 1):
            if Point(x, y) in SOLID_POINTS:
                print("#", end="")
            else:
                print(".", end="")
        print("")


if __name__ == "__main__":
    main02()
