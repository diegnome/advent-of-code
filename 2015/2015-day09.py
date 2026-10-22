# Advent of Code - 2015 - Day 09

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

input_parsed = {}
locations = []
for line in input_lines:
    m = re.search(r'(\w+) to (\w+) = (\d+)',line)
    if m.group(1) not in locations :
        locations.append(m.group(1))
    if m.group(2) not in locations :
        locations.append(m.group(2))
    input_parsed[(m.group(1),m.group(2))] = int(m.group(3))

# Input Pre-processing

def make_permutations(items):
    perm = []
    if len(items) == 1 :
        return [[items[0]]]
    # how to make permutations ?
    # take first element of list, and append all permutations of remaining ones
    for i in range(len(items)):
        remaining = items[:i]+items[i+1:]
        for permutation in make_permutations(remaining):
            perm.append([items[i]]+permutation)
    return perm

all_permutations = make_permutations(locations)

# Solution 1

shortest_distance = float("inf")

for permutation in tqdm(all_permutations):
    total_distance = 0
    for i in range(len(permutation)-1):
        if (permutation[i],permutation[i+1]) in input_parsed:
            total_distance += input_parsed[(permutation[i],permutation[i+1])]
        else:
            total_distance += input_parsed[(permutation[i+1],permutation[i])]
    if total_distance < shortest_distance:
        shortest_distance = total_distance

solution_1 = shortest_distance

# Solution 2

longest_distance = 0

for permutation in tqdm(all_permutations):
    total_distance = 0
    for i in range(len(permutation)-1):
        if (permutation[i],permutation[i+1]) in input_parsed:
            total_distance += input_parsed[(permutation[i],permutation[i+1])]
        else:
            total_distance += input_parsed[(permutation[i+1],permutation[i])]
    if total_distance > longest_distance:
        longest_distance = total_distance

solution_2 = longest_distance

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')