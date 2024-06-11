from loguru import logger


def look_and_say(initial_sequence: str, iterations: int) -> str:
    sequence: str = str(initial_sequence)
    next_sequence: str = ""

    for _ in range(iterations):
        curr_count: int = 1
        curr_digit: str = sequence[0]

        for char in sequence[1:]:
            if char != curr_digit:
                next_sequence += str(curr_count) + curr_digit

                curr_digit = char
                curr_count = 0

            curr_count += 1

        next_sequence += str(curr_count) + curr_digit
        sequence, next_sequence = next_sequence, ""

    return sequence


if __name__ == "__main__":
    INPUT: str = "1113122113"
    ITERATIONS: int = 50

    print(len(look_and_say(INPUT, ITERATIONS)))
