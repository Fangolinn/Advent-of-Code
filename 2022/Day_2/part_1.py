# https://adventofcode.com/2022/day/2

def points(moves: list):
    round_sum = 0
    
    if moves[1] == 'X':
        moves[1] = 'A'
    elif moves[1] == 'Y':
        moves[1] = 'B'
    elif moves[1] == 'Z':
        moves[1] = 'C'
        
    if moves[0] == moves[1]:
        round_sum += 3
    elif (moves[0] == 'A' and moves[1]== 'C') or (moves[0] == 'B' and moves[1]== 'A') or (moves[0] == 'C' and moves[1]== 'B'):
        round_sum += 0
    else:
        round_sum += 6
        
    values = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    
    return round_sum + values[moves[1]]
    

with open("2022\Day_2\input.txt", "r") as input_file:
    score = 0
    
    for line in input_file:
        moves = line.split()
        score += points(moves)
        
print(score) # expected out: 10310
    
    