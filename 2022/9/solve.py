# https://adventofcode.com/2022/day/9

from __future__ import annotations
import copy

from dataclasses import dataclass
from pathlib import Path

INPUT_FILE = "input.txt"


@dataclass
class Position:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        raise NotImplemented


def move(rope: list[Position], direction: str):
    match direction:
        case "U":
            rope[0].y += 1
        case "D":
            rope[0].y -= 1
        case "R":
            rope[0].x += 1
        case "L":
            rope[0].x -= 1
        case _:
            raise ValueError(
                "How the fuck did you even pass something wrong here as a direction."
            )

    # Update nodes other than head starging from the one nearest it
    for node, parent in zip(rope[1:], rope[:-1]):
        if abs(parent.x - node.x) > 2:
            raise Exception(
                "Something is fucked up, distance between parent and child node is more than 2."
            )

        if abs(parent.y - node.y) == 2 and abs(parent.x - node.x) == 2:
            # child node is two positions away diagonally
            node.x += int((parent.x - node.x) / 2)
            node.y += int((parent.y - node.y) / 2)
            continue

        # child node is away like knight in chess moves (two straight, one to the side)
        if abs(parent.x - node.x) == 2:
            node.y = parent.y

            node.x += int((parent.x - node.x) / 2)
            continue

        if abs(parent.y - node.y) == 2:
            node.x = parent.x

            node.y += int((parent.y - node.y) / 2)
            continue


def main(no_of_nodes: int):
    rope: list[Position] = [Position(0, 0) for _ in range(no_of_nodes)]
    tail_positions: list[Position] = []

    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        for line in input_file.readlines():
            move_definition = line.split()

            for _ in range(int(move_definition[1])):
                move(rope, move_definition[0])
                # print(rope)

                # if rope[-1] not in tail_positions:
                tail_positions.append(copy.deepcopy(rope[-1]))

    return len(set(tail_positions))


if __name__ == "__main__":
    # no_of_nodes = 2 # Part 1
    no_of_nodes = 10  # Part 2

    print(main(no_of_nodes))
