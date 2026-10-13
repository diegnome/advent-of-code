# Advent of Code - 2015 - Day 04

# Dependencies

from tqdm import tqdm
from pathlib import Path

from hashlib import md5

# Load Input

input_path =  Path(__file__).with_name(
    Path(__file__).stem + "-input.txt"
    )
input_text = input_path.read_text()

# Solution 1

decimal = 0
solution_found = False

# (this is to have the tqdm progress bar / timer working, thank you StackOverflow)
def gen():
    while not solution_found:
        yield

for _ in tqdm(gen()):
    decimal += 1
    hash_input = input_text + str(decimal)
    md5_hash = md5(hash_input.encode()).hexdigest()
    if md5_hash[:5] == '00000':
        solution_found = True

solution_1 = decimal

# Solution 2

decimal = 0
solution_found = False

for _ in tqdm(gen()):
    decimal += 1
    hash_input = input_text + str(decimal)
    md5_hash = md5(hash_input.encode()).hexdigest()
    if md5_hash[:6] == '000000':
        solution_found = True

solution_2 = decimal

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')