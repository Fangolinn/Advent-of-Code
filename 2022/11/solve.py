from __future__ import annotations

import math
from copy import deepcopy
from io import TextIOWrapper
from pathlib import Path

INPUT_FILE = "input.txt"
open(Path(__file__).parent / INPUT_FILE)


class Monkey:
    def __init__(self, monkey_def: list[str]) -> None:
        assert "Starting items: " in monkey_def[0]
        assert "Operation: " in monkey_def[1]
        assert "Test: " in monkey_def[2]
        assert "If true: " in monkey_def[3]
        assert "If false: " in monkey_def[4]

        self.items: list = [
            int(item)
            for item in monkey_def[0]
            .removeprefix("Starting items: ")
            .strip()
            .split(",")
        ]

        # How the fuck to parse 'operation?'
        self.operation = monkey_def[1].removeprefix("Operation: new = ").split(" ")

        # No support for other tests than "divisible by", make sure another option does not appear
        assert "divisible by" in monkey_def[2].removeprefix("Test: ")
        self.divisible_test = int(monkey_def[2].rsplit(maxsplit=1)[-1])

        self.target_true = int(monkey_def[3].rsplit(maxsplit=1)[-1])
        self.target_false = int(monkey_def[4].rsplit(maxsplit=1)[-1])

        self.inspection_count = 0

    def _do_operation(self, item_val: int) -> int:
        oper = deepcopy(self.operation)
        oper[0] = item_val if oper[0] == "old" else int(oper[0])  # type: ignore
        oper[2] = item_val if oper[2] == "old" else int(oper[2])  # type: ignore

        match oper[1]:
            case "+":
                return oper[0] + oper[2]
            case "*":
                return oper[0] * oper[2]

        raise NotImplementedError("Operand not handled")

    def inspect(self) -> None:
        self.items[0] = self._do_operation(self.items[0])
        self.inspection_count += 1

    def throw_to(self) -> int:
        if self.items[0] % self.divisible_test == 0:
            return self.target_true

        return self.target_false


def get_monkeys(input_file: TextIOWrapper) -> list[Monkey]:
    monkeys: list[Monkey] = []

    while True:
        # Extract single monkey definition
        monkey_def: list[str] = [input_file.readline().strip() for _ in range(6)]

        # Make sure we will assign correct number to the monkey
        assert int(monkey_def[0].strip(":").split()[1]) == len(monkeys)

        monkeys.append(Monkey(monkey_def[1:]))

        # Check if any more monkeys exist in the file (if we are at the end of the file)
        if input_file.readline() != "\n":
            break

    return monkeys


def main01(input_stream: TextIOWrapper):  # Part 1
    monkeys = get_monkeys(input_stream)

    for i in range(20):
        for monkey in monkeys:
            while len(monkey.items):
                monkey.inspect()
                monkey.items[0] = math.floor(monkey.items[0] / 3)
                target_monkey = monkey.throw_to()
                monkeys[target_monkey].items.append(monkey.items.pop(0))

        # print(f"Round {i +1}", [monkey.items for monkey in monkeys])

    insp_count = sorted([monkey.inspection_count for monkey in monkeys], reverse=True)
    return insp_count[0] * insp_count[1]


def main02(input_stream: TextIOWrapper):  # Part 2
    monkeys = get_monkeys(input_stream)

    least_common_divisor = math.lcm(*[monkey.divisible_test for monkey in monkeys])

    for i in range(10000):
        for monkey in monkeys:
            while len(monkey.items):
                monkey.inspect()
                monkey.items[0] = math.floor(monkey.items[0] % least_common_divisor)
                target_monkey = monkey.throw_to()
                monkeys[target_monkey].items.append(monkey.items.pop(0))

        # print(f"Round {i +1}", [monkey.items for monkey in monkeys])

    insp_count = sorted([monkey.inspection_count for monkey in monkeys], reverse=True)
    return insp_count[0] * insp_count[1]


if __name__ == "__main__":
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        print(main02(input_file))
