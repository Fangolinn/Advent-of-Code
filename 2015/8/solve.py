def count_characters(input_file: str) -> tuple[int, int]:
    """Returns a tuple of (string_repr_characters, in_memory_characters)"""

    string_repr_char_count: int = 0
    in_memory_char_count: int = 0

    with open(input_file) as file:
        while line := file.readline():
            string_repr_char_count += len(line.strip())
            in_memory_char_count += count_chars_in_memory(line.strip())

    return (string_repr_char_count, in_memory_char_count)


def count_characters_part_2(input_file: str) -> tuple[int, int]:
    """Returns a tuple of (encoded_char_count, original_char_count)"""

    string_repr_char_count: int = 0
    encoded_char_count: int = 0

    with open(input_file) as file:
        while line := file.readline():
            string_repr_char_count += len(line.strip())
            encoded_char_count += encoded_len(line.strip())

    return (encoded_char_count, string_repr_char_count)


def count_chars_in_memory(string: str) -> int:
    count: int = 0

    i: int = 0
    while i < len(string):
        if string[i] == '"':
            i += 1
            continue

        if string[i] == "\\":
            if string[i + 1] == "x":
                i += 3
            else:
                i += 1

        count += 1
        i += 1

    return count


def encoded_len(string: str) -> int:
    encodable_chars_count: int = 0

    for char in string:
        if char in '"\\':
            encodable_chars_count += 1

    return len(string) + encodable_chars_count + 2


if __name__ == "__main__":
    INPUT_FILE = "input.txt"

    # result = count_characters(INPUT_FILE)
    result = count_characters_part_2(INPUT_FILE)

    print(result[0] - result[1])
