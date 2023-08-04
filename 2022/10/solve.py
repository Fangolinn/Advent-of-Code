from io import TextIOWrapper
from pathlib import Path

INPUT_FILE = "input.txt"

KEY_CYCLES = [20, 60, 100, 140, 180, 220]

INSTRUCTION_LEN = {
    "addx": 2,
    "noop": 1
}

def main01(input_stream: TextIOWrapper):
    cycle_no = 0
    x_val = 1

    signal_strengths_sum = 0

    for line in input_stream.readlines():
        instruction = line.strip().split(" ")

        assert instruction[0] in INSTRUCTION_LEN.keys(), f"Actual instruction: {instruction[0]}"
        instruction_len = INSTRUCTION_LEN[instruction[0]]

        for _ in range(instruction_len):
            cycle_no += 1

            # Check if the current cycle is one of the 'key' ones
            if cycle_no in KEY_CYCLES:
                signal_strengths_sum += cycle_no * x_val

        if instruction[0] == "addx":
            x_val += int(instruction[1])

    return signal_strengths_sum

        

def main02(input_stream: TextIOWrapper):
    cycle_no = 0
    x_val = 1

    for line in input_stream.readlines():
        instruction = line.strip().split(" ")

        assert instruction[0] in INSTRUCTION_LEN.keys(), f"Actual instruction: {instruction[0]}"
        instruction_len = INSTRUCTION_LEN[instruction[0]]

        for _ in range(instruction_len):
            cycle_no += 1

            if (cycle_no % 40) - 1 in [x_val - 1, x_val, x_val + 1]:
                print("#", end="")
            else:
                print(".", end="")

            if cycle_no % 40 == 0:
                print("\n", end="")

        if instruction[0] == "addx":
            x_val += int(instruction[1])

        

if __name__ == "__main__":
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        print(main02(input_file))