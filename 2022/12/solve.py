from __future__ import annotations

import functools
import string
import time
from collections import namedtuple
from copy import deepcopy
from io import TextIOWrapper
from pathlib import Path

INPUT_FILE = "input.txt"

Point = namedtuple("Point", ["x", "y"])
Node = namedtuple("Node", ["point", "val"])
Route = list[Point]


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def parse_input(input: TextIOWrapper) -> list[list]:
    # Grab first line of the input, convert to list of lists.
    # Each sublist is a column in the input.
    terrain: list[list[str]] = [
        [char] for char in list(input.readline().strip())
    ]  # type: ignore

    for line in input.readlines():
        for column, new_entry in zip(terrain, list(line.strip())):
            column.append(new_entry)

    return terrain


with open(Path(__file__).parent / INPUT_FILE) as input_file:
    terrain = parse_input(input_file)


def get_coords(terrain: list[list[str]], char: str) -> Point:
    for col_no, column in enumerate(terrain):
        if char in column:
            return Point(col_no, column.index(char))

    raise ValueError("Not found")


def height(terrain: list[list[str]], node: Point) -> int:
    symbol: str = terrain[node.x][node.y]

    match symbol:
        case "S":
            symbol = "a"
        case "E":
            symbol = "z"

    return string.ascii_lowercase.index(symbol)


def get_neighbors(terrain: list[list[str]], node: Point) -> list[Point]:
    neighbors = []
    if node.x > 0:
        neighbors.append(Point(node.x - 1, node.y))

    if node.y > 0:
        neighbors.append(Point(node.x, node.y - 1))

    if node.x < len(terrain) - 1:
        neighbors.append(Point(node.x + 1, node.y))

    if node.y < len(terrain[0]) - 1:
        neighbors.append(Point(node.x, node.y + 1))

    return neighbors


def value(terrain: list[list[str]], node: Point) -> str:
    return terrain[node.x][node.y]


def find_path(
    terrain: list[list[str]], start: str = "S", end: str = "E", reverse: bool = False
):
    route_found = False
    routes = [[get_coords(terrain, start)]]
    prev_routes = len(routes)
    checked_nodes: set[Point] = set()

    end_node: Point = None

    step = 0

    while not route_found:
        print(
            f"Step: {step}",
            f"Routes: {len(routes)}",
            f"Ratio: {len(routes) / prev_routes}",
            sep=" | ",
        )
        step += 1
        prev_routes = len(routes)

        for route in reversed(routes):
            neighbors = list(
                set(get_neighbors(terrain, route[-1])) - set(route) - checked_nodes
            )

            # Remove neighbors that are too high
            for neighbor in reversed(neighbors):
                if (not reverse) and (
                    height(terrain, neighbor) > height(terrain, route[-1]) + 1
                ):
                    neighbors.remove(neighbor)
                    continue

                if reverse and (
                    height(terrain, route[-1]) - 1 > height(terrain, neighbor)
                ):
                    neighbors.remove(neighbor)
                    continue

            if not len(neighbors):
                routes.remove(route)
                continue

            for neighbor in neighbors:
                if end == value(terrain, neighbor):
                    route.append(neighbor)
                    end_node = neighbor
                    route_found = True
                    continue

            for neighbor in neighbors:
                routes.append([*deepcopy(route), neighbor])
                checked_nodes.add(neighbor)

            routes.remove(route)

    for route in reversed(routes):
        if end_node not in route:
            routes.remove(route)
            continue

    return routes


@timer
def main01(terrain: list[list[str]]):
    # FIXME - why is the route len too high by 2?
    print([route.__len__() - 2 for route in find_path(terrain)])


@timer
def main02(terrain: list[list[str]]):
    print([route.__len__() - 2 for route in find_path(terrain, "E", "a", reverse=True)])


if __name__ == "__main__":
    main02(terrain)
