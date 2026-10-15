# Advent of Code - 2015 - Day 07

# Dependencies

from tqdm import tqdm
from pathlib import Path

# Load Input

input_path =  Path(__file__).with_name(
    Path(__file__).stem + "-input.txt"
    )
input_text = input_path.read_text()
input_lines = input_text.splitlines()
input_parsed = {}
for line in input_lines:
    operation,output = line.split(' -> ')
    input_parsed[output] = operation.split(' ')

# Solution 1

cache = {}

def operation_result(wire):
    print(f'calculating for {wire}')
    if wire.isdigit():
        return int(wire)
    if wire not in cache :
        if len(input_parsed[wire]) == 1:
            result = operation_result(input_parsed[wire][0])
        else:
            operator = input_parsed[wire][-2] # index from end to account for NOT operator
            if operator == 'AND':
                result = operation_result(input_parsed[wire][0]) & operation_result(input_parsed[wire][2])
            elif operator == 'LSHIFT':
                result = operation_result(input_parsed[wire][0]) << operation_result(input_parsed[wire][2])
            elif operator == 'NOT':
                result = ~ operation_result(input_parsed[wire][1]) & 0b1111111111111111
            elif operator == 'OR':
                result = operation_result(input_parsed[wire][0]) | operation_result(input_parsed[wire][2])
            elif operator == 'RSHIFT':
                result = operation_result(input_parsed[wire][0]) >> operation_result(input_parsed[wire][2])
        cache[wire] = result
        return result
    else:
        return cache[wire]

solution_1 = operation_result('a')

# Solution 2

cache = {}
input_parsed['b'] = [str(solution_1)]

solution_2 = operation_result('a')

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')