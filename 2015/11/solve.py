# https://adventofcode.com/2015/day/11


from gettext import find


def is_valid_rule_contains_straight_of_letters(password: str) -> bool:
    """
    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz.
    They cannot skip letters; abd doesn't count.
    """
    for i in range(len(password) - 2):
        if (ord(password[i]) == ord(password[i + 1]) - 1) and (
            ord(password[i]) == ord(password[i + 2]) - 2
        ):
            return True

    return False


def is_valid_rule_no_forbidden_letters(password: str) -> bool:
    """
    Passwords may not contain the letters i, o, or l."""
    FORBIDDEN_LETTERS = "iol"

    for letter in FORBIDDEN_LETTERS:
        if letter in password:
            return False

    return True


def is_valid_rule_contains_two_pairs(password: str) -> bool:
    """
    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    """
    pairs_found: int = 0

    i: int = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs_found += 1
            i += 1

        if pairs_found >= 2:
            return True

        i += 1

    return False


def is_password_valid(password: str) -> bool:
    """Part 1 of the AoC problem"""
    return (
        is_valid_rule_no_forbidden_letters(password)
        and is_valid_rule_contains_two_pairs(password)
        and is_valid_rule_contains_straight_of_letters(password)
    )


def increment_string(string: str) -> str:
    """Increment string containing only lowercase letters. 'z' loops over to 'a' and carries to next most significant 'digit'"""
    string: str = string[::-1]
    new_string: str = ""

    i: int = 0
    carry: bool = True
    while carry and i < len(string):
        carry = True if string[i] == "z" else False
        new_string += chr((ord(string[i]) - ord("a") + 1) % 26 + ord("a"))

        i += 1

    if carry:
        new_string += "a"
    else:
        new_string += string[i:]

    return new_string[::-1]


def find_new_password(current_password: str) -> str:
    while not is_password_valid(current_password := increment_string(current_password)):
        pass

    return current_password


if __name__ == "__main__":
    INPUT: str = "vzbxkghb"

    part1_new_password = find_new_password(INPUT)
    part2_new_password = find_new_password(part1_new_password)

    print("Part 1:", part1_new_password)
    print("Part 2:", part2_new_password)
