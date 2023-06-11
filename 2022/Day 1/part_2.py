# https://adventofcode.com/2022/day/1#part2

with open("2022/1/input.txt", "r") as input_file:
    i = 0
    amounts = [0, 0]
    for line in input_file:
        if line == "\n":
            amounts.append(0)
            i += 1
            continue
        
        amounts[i] += int(line)
        
print(max(amounts))

sum = 0
for i in range(3):
    tmp = max(amounts)
    amounts.pop(amounts.index(tmp))
    sum += tmp
    
print(sum) # correct out: 212489