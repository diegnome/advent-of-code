# Advent of Code - 2015 - Day 01

# Dependencies

from tqdm import tqdm
from pathlib import Path

# Load Input

inputPath =  Path(__file__).with_name(
    Path(__file__).stem + "-input.txt"
    )
inputText = inputPath.read_text()

# Solution 1

floor = 0
for char in tqdm(inputText):
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1
solution_1 = floor

# Solution 2

floor = 0
basement_entry = None
for i in tqdm(range(len(inputText))):
    if inputText[i] == '(':
        floor += 1
    elif inputText[i] == ')':
        floor -= 1
    if basement_entry is None and floor < 0:
        basement_entry = i+1
solution_2 = basement_entry

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')