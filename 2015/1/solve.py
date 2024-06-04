from pathlib import Path

INPUT_FILE = "input.txt"

if __name__ == "__main__":
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        instructions = input_file.readline()

    # part 1
    # print(instructions.count("(") - instructions.count(")"))

    floor = 0
    for instr_no in range(len(instructions)):
        match instructions[instr_no]:
            case "(":
                floor += 1
            case ")":
                floor -= 1
            case _:
                raise ValueError

        if floor < 0:
            print(f"Entered floor {floor} at pos {instr_no + 1}")
            break
