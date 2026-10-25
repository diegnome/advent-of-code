# Advent of Code - 2015 - Day 11

# Dependencies

from tqdm import tqdm
from pathlib import Path

# Load Input

input_path =  Path(__file__).with_name(
    Path(__file__).stem + "-input.txt"
    )
input_text = input_path.read_text()
input_lines = input_text.splitlines()

# Solution 1

letters = 'abcdefghijklmnopqrstuvwxyz'

def increment_string(str_s):
    s = list(str_s)
    for i in range(-1,-len(s)-1,-1):
        if s[i] == 'z':
            s[i] = 'a'
        else:
            s[i] = letters[letters.index(s[i])+1]
            return ''.join(s)

current_password = input_lines[0]

while True:
    current_password = increment_string(current_password)

    has_iol = 'i' in current_password or 'o' in current_password or 'l' in current_password
    if has_iol:
        continue
    
    has_straight = any([current_password[i:i+3] in letters
                       for i in range(len(current_password)-2)])
    if not has_straight:
        continue
    
    has_double_pair = False
    for i in range(1,len(current_password)-1):
        if has_double_pair:
            break
        for j in range(1,len(current_password)-1):
            if (current_password[j] == current_password[j+1]
                and current_password[i] == current_password[i+1]
                and abs(j-i) >= 2) :
                has_double_pair = True
    if not has_double_pair:
        continue

    break

solution_1 = current_password

# Solution 2

while True:
    current_password = increment_string(current_password)

    has_iol = 'i' in current_password or 'o' in current_password or 'l' in current_password
    if has_iol:
        continue
    
    has_straight = any([current_password[i:i+3] in letters
                       for i in range(len(current_password)-2)])
    if not has_straight:
        continue
    
    has_double_pair = False
    for i in range(1,len(current_password)-1):
        if has_double_pair:
            break
        for j in range(1,len(current_password)-1):
            if (current_password[j] == current_password[j+1]
                and current_password[i] == current_password[i+1]
                and abs(j-i) >= 2) :
                has_double_pair = True
    if not has_double_pair:
        continue

    break

solution_2 = current_password

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')