from parse import search

COLORS = ["red", "green", "blue"]

# PARSERS:

GamesInfo = dict[int, list[dict]]


def parse_input(input_file: str) -> GamesInfo:
    parsed: GamesInfo = dict()

    with open(input_file) as file:
        while line := file.readline():
            game_no = search("Game {:d}:", line)[0]
            parsed[game_no] = list()

            for round in line.split(";"):
                round_record = dict()
                for color in COLORS:
                    color_count: int | None = search("{:d} " + color, round)

                    if color_count is not None:
                        round_record[color] = color_count[0]

                parsed[game_no].append(round_record)

    return parsed


if __name__ == "__main__":
    INPUT_FILE = "input_example.txt"

    print(parse_input(INPUT_FILE))
