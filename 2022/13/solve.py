import itertools
import re
from pathlib import Path

INPUT_FILE = "input.txt"
LIST_PATTERN = re.compile("\\[.*\\]")


def parse_to_items(line: str) -> list[str]:
    line = line.strip("\n")
    line_split: list[str] = line.split(",")
    final_chars: list[str] = []

    for item in line_split:
        brackets_before = [char for char in item if char == "["]
        brackets_after = [char for char in item if char == "]"]

        item = item.strip("[]")
        number = int(item) if item else None

        final_chars.extend(itertools.chain(brackets_before, [number], brackets_after))

    return final_chars


def parse_list(chars: list[str] | str, parsed=False) -> list:
    if not parsed:
        chars = parse_to_items(chars)

    chars = chars[1:]

    parsed = []

    i = 0

    while i < len(chars):
        char = chars[i]

        if isinstance(char, int):
            parsed.append(char)

        if char == "[":
            temp = i

            x = 1
            while x != 0:
                i += 1
                match chars[i]:
                    case "[":
                        x += 1
                    case "]":
                        x -= 1

            chars_inner: str = chars[temp : i + 1]

            parsed.append(parse_list(chars_inner, parsed=True))

        i += 1

    return parsed


def compare(left_packet: list, right_packet: list) -> bool:
    for left, right in zip(left_packet, right_packet):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True

            if left > right:
                return False

        if isinstance(left, list) and isinstance(right, list):
            inner_compare = compare(left, right)

            if isinstance(inner_compare, bool):
                return inner_compare

        if isinstance(left, int) and isinstance(right, list):
            inner_compare = compare([left], right)

            if isinstance(inner_compare, bool):
                return inner_compare

        if isinstance(left, list) and isinstance(right, int):
            inner_compare = compare(left, [right])

            if isinstance(inner_compare, bool):
                return inner_compare

    if len(left_packet) < len(right_packet):
        return True

    if len(left_packet) > len(right_packet):
        return False

    return 0


# Part 1
def main01() -> None:
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        current_pair = 1
        correct_pairs = []

        while True:
            first_line = input_file.readline()
            second_line = input_file.readline()

            if compare(
                parse_list(first_line),
                parse_list(second_line),
            ):
                correct_pairs.append(current_pair)

            if not input_file.readline():
                break

            current_pair += 1

        print("Out: ", sum(correct_pairs))


# Part 2
def main02() -> None:
    DIVIDER_PACKETS: list = [[[2]], [[6]]]

    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        # Grab all packets to a single list
        packets = []
        while True:
            line = input_file.readline()

            if line == "\n":
                continue

            if not line:
                break

            packets.append(parse_list(line))

    packets.extend(DIVIDER_PACKETS)

    def bubble_sort(lst):
        n = len(lst)
        for i in range(n):
            for j in range(0, n - i - 1):  # Last i elements are already in place
                if not compare(
                    lst[j], lst[j + 1]
                ):  # Swap if the element found is greater than the next element
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst

    bubble_sort(packets)

    divider_index = [packets.index(div_packet) + 1 for div_packet in DIVIDER_PACKETS]

    print("Out:", divider_index[0] * divider_index[1])


if __name__ == "__main__":
    main02()
