# https://adventofcode.com/2022/day/1

with open("2022/1/input.txt", "r") as input_file:
    i = 0
    amounts = [0, 0]
    for line in input_file:
        if line == "\n":
            amounts.append(0)
            i += 1
            continue
        
        amounts[i] += int(line)
        
print(max(amounts)) # correct out: 71780