from pathlib import Path

INPUT_FILE = "input.txt"


def part1(boxes: list[list[int]]) -> int:
    paper_required = 0
    for box in boxes:
        side_areas = [box[0] * box[1], box[1] * box[2], box[2] * box[0]]
        min_area = min(side_areas)
        paper_required += 2 * sum(side_areas) + min_area

    return paper_required


def part2(boxes: list[list[int]]) -> int:
    ribbon_required = 0
    for box in boxes:
        # bow
        ribbon_required += box[0] * box[1] * box[2]

        # wrap
        box.sort()
        ribbon_required += (box[0] + box[1]) * 2

    return ribbon_required


if __name__ == "__main__":
    with open(Path(__file__).parent / INPUT_FILE) as input_file:
        boxes: list[list[int]] = []
        for line in input_file.readlines():
            boxes.append(list(map(int, line.split("x"))))

    print(part2(boxes))
