# https://adventofcode.com/2022/day/5

from pathlib import Path

input_file = open(Path(__file__).parent / "input.txt")

starting_stacks = []
while True:
    line = input_file.readline()

    if line == "\n":
        break

    starting_stacks.append(line)

starting_stacks_parsed = []

for level in starting_stacks[-2::-1]:
    starting_stacks_parsed.append(level[1::4])

stacks_amount = len(starting_stacks_parsed[0])
stacks: list[list] = [[] for _ in range(stacks_amount)]

for level in starting_stacks_parsed:
    for item, stack_no in zip(level, range(stacks_amount)):
        stacks[stack_no].append(item) if item != " " else None


def move_item(command: str):
    """
    Expected command format:
        'move n from x to y'

        n - amount of items to move
        x - source stack
        y - destination stack
    """
    cmd = command.split(" ")
    amount, start_stack, dest_stack = int(cmd[1]), int(cmd[3]), int(cmd[5])

    for _ in range(amount):
        # -1 for each stack number to offset indexing (starting from 0)
        item = stacks[start_stack - 1].pop()
        stacks[dest_stack - 1].append(item)


for line in input_file.readlines():
    move_item(line)

print("".join([stack[-1] for stack in stacks]))

input_file.close()
