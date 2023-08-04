# https://adventofcode.com/2022/day/8

from pathlib import Path

def load_data(target: list = []) -> list[list[int]]:
    # Keep input data as a 2-dimensional list
    with open(Path(__file__).parent / "input.txt") as input_file:
        for line in input_file.readlines():
            if line == "\n":
                break

            row = [int(tree) for tree in list(line.strip("\n"))]
            target.append(row)

    return target

def is_visible(forest: list[list[int]], row_no: int, column_no: int) -> bool:
    current_tree_height = forest[row_no][column_no]

    # Trees on the edges are always visible
    if row_no == 0 or row_no == len(forest) - 1:
        return True
    
    if column_no == 0 or column_no == len(forest[0]) - 1:
        return True

    # Check visibility from the left
    if max(forest[row_no][:column_no]) < current_tree_height:
        return True
    
    # Check visibility from the right
    if max(forest[row_no][:column_no:-1]) < current_tree_height:
        return True
    
    # Extract current column for vertical checks
    column = []
    for row in forest:
        column.append(row[column_no])

    # Check visibility from the top
    if max(column[:row_no]) < current_tree_height:
        return True
    
    # Check visibility from the bottom
    if max(column[:row_no:-1]) < current_tree_height:
        return True
    
    return False


def main01(): # Part 1
    # I will be using the naive method - for each 'tree' check if it's visible from any side
    # More efficient method exists for sure
    forest = load_data()

    visible = 0

    for row_no, row in enumerate(forest):
        for column_no, column in enumerate(row):
            if is_visible(forest, row_no, column_no):
                visible += 1

    return visible

# Part 2

def visible_trees(trees_sequence: list[int], current_tree: int):
    try:
        return trees_sequence.index(next(tree for tree in trees_sequence if tree >= current_tree)) + 1
    except StopIteration:
        return len(trees_sequence)

def scenic_score(forest: list[list[int]], row_no: int, column_no: int) -> int:
    current_tree_height = forest[row_no][column_no]

    # Trees on the edges always have a scenic score of 0
    if row_no == 0 or row_no == len(forest) - 1:
        return 0
    
    if column_no == 0 or column_no == len(forest[0]) - 1:
        return 0
    
    score = 1

    # Extract current column for vertical checks
    column = []
    for row in forest:
        column.append(row[column_no])

    # Get visibility up
    score *= visible_trees(list(reversed(column[:row_no])), current_tree_height)

    # Get visibility down
    score *= visible_trees(list(reversed(column[:row_no:-1])), current_tree_height)

    # Get visibility up
    score *= visible_trees(list(reversed(forest[row_no][:column_no])), current_tree_height)

    # Get visibility up
    score *= visible_trees(list(reversed(forest[row_no][:column_no:-1])), current_tree_height)

    return score

def main02(): # Part 2
    forest = load_data()

    scores = []

    for row_no, row in enumerate(forest):
        for column_no, column in enumerate(row):
            scores.append(scenic_score(forest, row_no, column_no))

    return max(scores)


if __name__ == "__main__":
    print(main02())