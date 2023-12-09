import re
import math

network = {}
regex = r"(...) = \((...), (...)\)"

with open("8.in") as input_file:
    instructions = input_file.readline().strip()

    lines = [s.strip() for s in input_file.readlines()]
    lines = [s for s in lines if s]

    for line in lines:
        g = re.search(regex, line).groups()
        network[g[0]] = {"L":g[1], "R": g[2]}
  
def count_steps(start):
    instruction = 0
    steps = 0
    curr_pos = start
    while curr_pos[-1] != "Z":

        next_instruction = instructions[instruction]
        instruction = (instruction + 1) % len(instructions)

        curr_pos = network[curr_pos][next_instruction]
        steps += 1
    return steps

def count_steps_all(starts):
    steps = []
    for start in starts:
        steps.append(count_steps(start))
    return math.lcm(*steps)
        
start_positions = []
for k in network:
    if k[-1] == "A":
        start_positions.append(k)

total_steps = count_steps_all(start_positions)
        
print(total_steps)
