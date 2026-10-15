# Advent of Code - 2015 - Day 06

# Dependencies

from tqdm import tqdm
from pathlib import Path
import re

# Load Input

input_path =  Path(__file__).with_name(
    Path(__file__).stem + "-input.txt"
    )
input_text = input_path.read_text()
input_lines = input_text.splitlines()
input_parsed = []
for line in input_lines:
    m = re.search(r'(turn on|turn off|toggle) (\d*),(\d*) through (\d*),(\d*)',line)
    input_parsed.append((m.group(1),(int(m.group(2)),int(m.group(3))),(int(m.group(4)),int(m.group(5)))))

# Solution 1

grid = [[0 for x in range(1000)]for y in range(1000)]

for inst in tqdm(input_parsed):
    if inst[0] == 'turn on':
        for x in range(inst[1][0],inst[2][0]+1):
            for y in range(inst[1][1],inst[2][1]+1):
                grid[y][x] = 1
    elif inst[0] == 'turn off':
        for x in range(inst[1][0],inst[2][0]+1):
            for y in range(inst[1][1],inst[2][1]+1):
                grid[y][x] = 0
    elif inst[0] == 'toggle':
        for x in range(inst[1][0],inst[2][0]+1):
            for y in range(inst[1][1],inst[2][1]+1):
                grid[y][x] = (grid[y][x] + 1) % 2

lights_count = sum([sum(row) for row in grid])

solution_1 = lights_count

# Solution 2

grid = [[0 for x in range(1000)]for y in range(1000)]

for inst in tqdm(input_parsed):
    if inst[0] == 'turn on':
        for x in range(inst[1][0],inst[2][0]+1):
            for y in range(inst[1][1],inst[2][1]+1):
                grid[y][x] += 1
    elif inst[0] == 'turn off':
        for x in range(inst[1][0],inst[2][0]+1):
            for y in range(inst[1][1],inst[2][1]+1):
                grid[y][x] = max(0,grid[y][x]-1)
    elif inst[0] == 'toggle':
        for x in range(inst[1][0],inst[2][0]+1):
            for y in range(inst[1][1],inst[2][1]+1):
                grid[y][x] += 2

brightness_total = sum([sum(row) for row in grid])

solution_2 = brightness_total

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')