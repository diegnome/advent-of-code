# Advent of Code - 2015 - Day 02

# Dependencies

from tqdm import tqdm
from pathlib import Path

# Load Input

input_path =  Path(__file__).with_name(
    Path(__file__).stem + "-input.txt"
    )
input_text = input_path.read_text()
input_lines = input_text.splitlines()
input_parsed = [[int(dimension) for dimension in line.split('x')] for line in input_lines]

# Solution 1

total_surface = 0

for present in tqdm(input_parsed):
    l_w = present[0]*present[1] # face surfaces
    w_h = present[1]*present[2]
    h_l = present[2]*present[0]
    slack = min(l_w,w_h,h_l)
    present_paper = 2*l_w + 2*w_h + 2*h_l + slack
    total_surface += present_paper

solution_1 = total_surface

# Solution 2

total_length = 0

for present in tqdm(input_parsed):
    volume = present[0]*present[1]*present[2]
    p1 = 2*(present[0]+present[1]) # face perimeters
    p2 = 2*(present[1]+present[2])
    p3 = 2*(present[2]+present[0])
    smallest_perimeter = min(p1,p2,p3)
    ribbon_length = smallest_perimeter + volume
    total_length += ribbon_length

solution_2 = total_length

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')