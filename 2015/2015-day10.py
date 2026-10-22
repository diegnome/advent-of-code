# Advent of Code - 2015 - Day 10

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

iterations = input_lines[0]

for i in tqdm(range(40)):
    prev_line = iterations
    next_line = ""
    last_count = 1
    for j in range(1,len(prev_line)):
        if prev_line[j] != prev_line[j-1]:
            next_line += str(last_count) + prev_line[j-1]
            last_count = 1
        else:
            last_count += 1
    next_line += str(last_count) + prev_line[-1]
    iterations = next_line

solution_1 = len(iterations[-1])

# Solution 2

# we continue expanding on iterations !

for i in tqdm(range(10)):
    prev_line = iterations
    next_line = ""
    last_count = 1
    for j in range(1,len(prev_line)):
        if prev_line[j] != prev_line[j-1]:
            next_line += str(last_count) + prev_line[j-1]
            last_count = 1
        else:
            last_count += 1
    next_line += str(last_count) + prev_line[-1]
    iterations = next_line

solution_2 = len(iterations[-1])

# takes so long ?!!

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')