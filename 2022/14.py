def get_bounds(grid : dict):
    minx, miny = 1000, 1000
    maxx, maxy = 0, 0
    for pos in grid:
        minx = min(pos[0], minx)
        miny = min(pos[1], miny)
        maxx = max(pos[0], maxx)
        maxy = max(pos[1], maxy)
    return minx, miny, maxx, maxy
        
def draw_grid(grid : dict):
    minx, miny, maxx, maxy = get_bounds(grid)
    for y in range(miny - 1, maxy + 2):
        print("{0:>2} ".format(y), end="")
        for x in range(minx - 1, maxx + 2):
            if (x,y) in grid:
                print(grid[(x, y)], end="") 
            else:
                print(".", end="")
        print()


def generate_grid():
    data = [l.strip() for l in open("14.txt")]
    grid = {}
    for line in data:
        coords = line.split(" -> ")
        for i in range(len(coords) - 1):
            p1 = [int(x) for x in coords[i].split(",")]
            p2 = [int(x) for x in coords[i + 1].split(",")]
            if p1[0] == p2[0]:
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    grid[(p1[0], y)] = '#'
            else:
                for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                    grid[(x, p1[1])] = '#'
    return grid

def next_position(grid: dict, position: tuple):
    if (position[0], position[1] + 1) not in grid:
        return (position[0], position[1] + 1)
    elif (position[0] - 1, position[1] + 1) not in grid:
        return (position[0] - 1, position[1] + 1)
    elif (position[0] + 1, position[1] + 1) not in grid:
        return (position[0] + 1, position[1] + 1)
    else:
        return None

def place_sand(grid : dict):
    current_pos = (500, 0)

    while True:
       next_pos = next_position(grid, current_pos)
       if next_pos == None:
           grid[current_pos] = "o"
           return True
       else:
           current_pos = next_pos
       if current_pos[1] > 1000:
           return False

# Part 2
def place_sand_with_floor(grid : dict, floor_level : int):
    current_pos = (500, 0)

    while True:
       next_pos = next_position(grid, current_pos)
       if next_pos == None:
           grid[current_pos] = "o"
           return True
       else:
           current_pos = next_pos
       if current_pos[1] == floor_level:
           grid[current_pos] = "o"
           return True
    
grid = generate_grid()
x,x,x,floor_level = get_bounds(grid)
floor_level += 1
count = 0
while True:
    if not place_sand(grid):
        break
    count += 1

print("Part 1 answer:", count)

while True:
    place_sand_with_floor(grid, floor_level)

    count += 1
    if (500, 0) in grid:
        break
draw_grid(grid)
print("Part 2 answer:", count)
