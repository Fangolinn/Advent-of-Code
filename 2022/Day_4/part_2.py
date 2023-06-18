# https://adventofcode.com/2022/day/4#part2

from collections import namedtuple


Range = namedtuple("Range", ["start", "end"])

def parse_line(line: str) -> tuple[Range, Range]:
    line = line.strip().split(",")

    boundries1, boundries2 = line[0].split("-"), line[1].split("-")
    return (Range(int(boundries1[0]), int(boundries1[1])), Range(int(boundries2[0]), int(boundries2[1])))

def ranges_overlap(range1: Range, range2: Range) -> bool:
    if range1.start <= range2.end and range1.start >= range2.start:
        return True
    
    if range2.start <= range1.end and range2.start >= range1.start:
        return True
    
    return False

count: int = 0

with open("./2022/Day_4/input.txt") as input_file:
    for line in input_file.readlines():
        range1, range2 = parse_line(line)
        count += int(ranges_overlap(range1, range2))

print("Result:", count)
        