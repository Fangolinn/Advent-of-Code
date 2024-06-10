from enum import Enum, auto
from inspect import getblock

from parse import parse


class Instruction(str, Enum):
    TURN_ON = "turn on "
    TOGGLE = "toggle "
    TURN_OFF = "turn off "


Board = dict[tuple[int, int], int]


def parse_input(input_file: str) -> list[list]:
    instructions: list[list] = []

    with open(input_file) as file:
        for line in file.readlines():
            for prefix in Instruction:
                if line.find(prefix.value) == 0:
                    line = line.removeprefix(prefix.value)
                    instruction = [prefix]

                    parsed = parse(
                        "{starti:d},{startj:d} through {endi:d},{endj:d}", line.strip()
                    )
                    instruction.append((parsed["starti"], parsed["startj"]))
                    instruction.append((parsed["endi"], parsed["endj"]))

                    instructions.append(instruction)

    return instructions


def execute_instructions(instructions: list[list], board: Board) -> None:
    for instruction in instructions:
        for i in range(instruction[1][0], instruction[2][0] + 1):
            for j in range(instruction[1][1], instruction[2][1] + 1):
                match instruction[0]:
                    case Instruction.TURN_ON:
                        board[(i, j)] = 1
                    case Instruction.TURN_OFF:
                        board[(i, j)] = 0
                    case Instruction.TOGGLE:
                        board[(i, j)] = 1 if board[(i, j)] == 0 else 0
                    case _:
                        raise ValueError("Did not match anything!", instruction[0])


def count_turned_on(board: Board, size: int) -> int:
    count: int = 0

    for i in range(size):
        for j in range(size):
            count += 1 if board[(i, j)] == 1 else 0

    return count


def execute_instructions_part2(instructions: list[list], board: Board) -> None:
    for instruction in instructions:
        for i in range(instruction[1][0], instruction[2][0] + 1):
            for j in range(instruction[1][1], instruction[2][1] + 1):
                match instruction[0]:
                    case Instruction.TURN_ON:
                        board[(i, j)] += 1
                    case Instruction.TURN_OFF:
                        board[(i, j)] -= 1 if board[(i, j)] > 0 else 0
                    case Instruction.TOGGLE:
                        board[(i, j)] += 2
                    case _:
                        raise ValueError("Did not match anything!", instruction[0])


def combined_brightness(board: Board, size: int) -> int:
    combined: int = 0

    for i in range(size):
        for j in range(size):
            combined += board[(i, j)]

    return combined


def get_board(size: int) -> Board:
    board: Board = dict()

    for i in range(size):
        for j in range(size):
            board[(i, j)] = 0

    return board


if __name__ == "__main__":
    BOARD_SIZE = 1000

    board: Board = get_board(BOARD_SIZE)

    instructions = parse_input("input.txt")

    assert combined_brightness(board, BOARD_SIZE) == 0

    execute_instructions_part2(instructions, board)

    print(combined_brightness(board, BOARD_SIZE))
