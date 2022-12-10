from math import sqrt
from math import copysign

def dist(t1, t2):
    return sqrt( (t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2 )

def dir_vec(t1, t2):
    l = dist(t1, t2)
    return ((t2[0] - t1[0]) / l, (t2[1] - t1[1]) / l )

def move_knot(original_pos, next_knot_pos):
    dir_vector = dir_vec(original_pos, next_knot_pos)
    new_knot_pos = (original_pos[0] + (int(copysign(1, dir_vector[0])) if abs(dir_vector[0]) > 0 else 0), original_pos[1] + (int(copysign(1, dir_vector[1])) if abs(dir_vector[1]) > 0 else 0))
    return new_knot_pos

def move_knots(knot_positions):
    for i in range(1, len(knot_positions)):
        if (dist(knot_positions[i-1], knot_positions[i]) > sqrt(2) + 0.01):
            knot_positions[i] = move_knot(knot_positions[i], knot_positions[i-1])
            
def print_knots(structure):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    for v in structure:
        min_x = min(min_x, v[0])
        max_x = max(max_x, v[0])
        min_y = min(min_y, v[1])
        max_y = max(max_y, v[1])

    for y in range( max_y + 2,min_y - 2,-1):
        for x in range(min_x - 2, max_x + 2):
            pos = (x, y)
            if x == 0 and y == 0:
                print("s", end="")
            elif pos in structure:
                print("#", end="")
            else:
                print(".", end="")
        print("")
        
    
data = open("9.txt")

structure = set()

nr_knots = 10
head_pos = (0,0)
tail_pos = (0,0)
knot_positions = [(0,0)] * nr_knots

for line in data:
    direction, length = line.split()
    length = int(length)
    structure.add(tail_pos)

    for i in range(length):
        if direction == "R":
            knot_positions[0] = (knot_positions[0][0] + 1, knot_positions[0][1])
        
        if direction == "L":
            knot_positions[0] = (knot_positions[0][0] - 1, knot_positions[0][1])
        
        if direction == "U":
            knot_positions[0] = (knot_positions[0][0], knot_positions[0][1] + 1)
        
        if direction == "D":
            knot_positions[0] = (knot_positions[0][0], knot_positions[0][1] - 1)
        
        move_knots(knot_positions)
        structure.add(knot_positions[-1])
    
print_knots(structure)
print(len(structure))
