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

nice_count = 0

for string in tqdm(input_lines):
    has_double_pair = False
    for i in range(1,len(string)-1):
        if has_double_pair:
            break
        pair = string[i]+string[i+1]
        for j in range(i):
            if string[j]+string[j+1] == pair and j<=i-2:
                has_double_pair = True
    has_sandwich = any([string[i] == string[i+2] for i in range(len(string)-2)])
    is_nice = has_double_pair and has_sandwich
    if is_nice:
        nice_count += 1

solution_2 = nice_count

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')