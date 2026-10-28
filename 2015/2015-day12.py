# Advent of Code - 2015 - Day 12

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
input_parsed = input_lines[0]

# Solution 1

all_numbers = [int(n) for n in tqdm(re.findall(r'-?\d+',input_parsed))]

solution_1 = sum(all_numbers)

# Solution 2

solution_2 = None

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')