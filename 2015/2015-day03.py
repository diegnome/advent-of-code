# Advent of Code - 2015 - Day 03

# Dependencies

from tqdm import tqdm
from pathlib import Path

# Load Input

input_path =  Path(__file__).with_name(
    Path(__file__).stem + "-input.txt"
    )
input_text = input_path.read_text()

# Solution 1

visited_houses = [(0,0)]

santa_x = 0
santa_y = 0

for dir in tqdm(input_text):
    # Move santa
    if dir == 'v':
        santa_y -= 1
    elif dir == '^':
        santa_y += 1
    elif dir == '<':
        santa_x -= 1
    elif dir == '>':
        santa_x += 1
    # Drop present
    santa_coords = (santa_x,santa_y)
    if santa_coords not in visited_houses:
        visited_houses.append(santa_coords)

solution_1 = len(visited_houses)

# Solution 2

visited_houses = [(0,0)]

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0

for i in tqdm(range(0,len(input_text),2)):
    santa_dir = input_text[i]
    robo_dir = input_text[i+1]
    # Move santa
    if santa_dir == 'v':
        santa_y -= 1
    elif santa_dir == '^':
        santa_y += 1
    elif santa_dir == '<':
        santa_x -= 1
    elif santa_dir == '>':
        santa_x += 1
    # Move robo
    if robo_dir == 'v':
        robo_y -= 1
    elif robo_dir == '^':
        robo_y += 1
    elif robo_dir == '<':
        robo_x -= 1
    elif robo_dir == '>':
        robo_x += 1
    # Drop present
    santa_coords = (santa_x,santa_y)
    robo_coords = (robo_x,robo_y)
    if santa_coords not in visited_houses:
        visited_houses.append(santa_coords)
    if robo_coords not in visited_houses:
        visited_houses.append(robo_coords)

solution_2 = len(visited_houses)

# Output

print(f'Solution 1 is:\n{solution_1}')
print(f'Solution 2 is:\n{solution_2}')