# Advent of Code - 2015 - Day 05

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

nice_count = 0

vowels = 'aeiou'
forbidden = ['ab','cd','pq','xy']

for string in tqdm(input_lines):
    has_three_vowels = [letter in vowels for letter in string].count(True) >= 3
    has_double_letters = any([string[i] == string[i+1] for i in range(len(string)-1)])
    contains_forbidden = any([substr in string for substr in forbidden])
    is_nice = has_three_vowels and has_double_letters and not contains_forbidden
    if is_nice:
        nice_count += 1

solution_1 = nice_count

# Solution 2

solution_2 = None

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')