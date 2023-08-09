# https://adventofcode.com/2022/day/3#part2


def get_item_priority(item: str):
    char = item[0]

    if char.isupper():
        return ord(char) - 64 + 26
    if char.islower():
        return ord(char) - 96

    raise ValueError("Not a viable ascii character")


def main():
    badges = []

    with open("./2022/Day_3/input.txt", "r") as input_file:
        backpacks = input_file.readlines()

        for elf1, elf2, elf3 in zip(backpacks[::3], backpacks[1::3], backpacks[2::3]):
            elf1, elf2, elf3 = elf1.strip("\n"), elf2.strip("\n"), elf3.strip("\n")

            for item in elf1:
                if item in elf2 and item in elf3:
                    badges.append(item)
                    break

    print(sum([get_item_priority(item) for item in badges]))  # correct out - 8202


if __name__ == "__main__":
    main()
