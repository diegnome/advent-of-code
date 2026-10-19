# Advent of Code - 2015 - Day 08

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

string_total = 0
memory_total = 0

for line in tqdm(input_lines):
    string_length = len(line)
    memory_length = len(line)
    memory_length -= 2 # initial and final " "
    i = 1
    while i < len(line)-1:
        if line[i]+line[i+1] == r'\\':
            memory_length -= 1
            i += 2
        elif line[i]+line[i+1] == r'\"':
            memory_length -= 1
            i += 2
        elif line[i]+line[i+1] == r'\x':
            memory_length -= 3
            i += 4
        else :
            i += 1
    string_total += string_length
    memory_total += memory_length

solution_1 = string_total - memory_total

# Solution 2

original_total = 0
encoded_total = 0

for line in tqdm(input_lines):
    original_length = len(line)
    encoded_length = len(line)
    encoded_length += 2 # initial and final " "
    for char in line:
        if char == r'"' or char == '\\':
            encoded_length += 1
    original_total += original_length
    encoded_total += encoded_length

solution_2 = encoded_total - original_total

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')