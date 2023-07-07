# https://adventofcode.com/2022/day/2#part2

def points(moves: list): 
    values_abc = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    
    values_xyz = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }
    
    loss_dict = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }
    
    win_dict = {
        'C': 'A',
        'A': 'B',
        'B': 'C'
    }
    
    round_sum = values_xyz[moves[1]]
    
    if round_sum == 0:
        round_sum += values_abc[loss_dict[moves[0]]]
    elif round_sum == 6:
        round_sum += values_abc[win_dict[moves[0]]]
    else:
        round_sum += values_abc[moves[0]]
        
    return round_sum
    

with open("2022/2/input.txt", "r") as input_file:
    score = 0
    
    for line in input_file:
        moves = line.split()
        score += points(moves)
        
print(score) # expected out: 14859
    
    