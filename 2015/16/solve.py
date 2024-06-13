# https://adventofcode.com/2015/day/16

from parse import Parser, Result, compile, search

POSSIBLE_STATS: list[str] = [
    "children",
    "cats",
    "samoyeds",
    "pomeranians",
    "akitas",
    "vizslas",
    "goldfish",
    "trees",
    "cars",
    "perfumes",
]

AuntStats = dict[str, int]
AuntsInfo = dict[str, AuntStats]


def create_parsers(keys: list[str]) -> dict[str, Parser]:
    return {key: compile(key + ": {:d},") for key in keys}


def parse_single_line(line: str, parsers: dict[str, Parser]) -> AuntsInfo:
    """Parse a single line, returns AuntsInfo with only a single aunt in it"""

    aunt_id: str = search("Sue {id}:", line)["id"]
    parsed: AuntsInfo = {aunt_id: dict()}

    line: str = line.strip() + ","

    for stat_name, parser in parsers.items():
        stat_val: Result | None = parser.search(line)

        if stat_val is not None:
            parsed[aunt_id][stat_name] = stat_val[0]

    return parsed


def parse_input(input_file: str) -> AuntsInfo:
    parsed: AuntsInfo = dict()

    with open(input_file) as file:
        parsers: dict[str, Parser] = create_parsers(POSSIBLE_STATS)

        while line := file.readline():
            parsed |= parse_single_line(line, parsers)

    return parsed


def find_matching(target: AuntStats, data: AuntsInfo) -> list[str]:
    matching: list[str] = list()

    for id, stats in data.items():
        matches: bool = True
        for stat_name, stat_val in stats.items():
            if stat_name in target:
                match stat_name:
                    case "cats" | "trees":
                        matches = stat_val > target[stat_name]
                    case "pomeranians" | "goldfish":
                        matches = stat_val < target[stat_name]
                    case _:
                        matches = stat_val == target[stat_name]

                if not matches:
                    break

        if matches:
            matching.append(id)

    return matching


if __name__ == "__main__":
    INPUT: str = "input.txt"
    TARGET: AuntStats = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    parsed: AuntsInfo = parse_input(INPUT)
    result: list[str] = find_matching(TARGET, parsed)
    print(result)
    for id in result:
        print(parsed[id])
