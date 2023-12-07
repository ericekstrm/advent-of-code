from termcolor import colored
from random import randint

shapes = []
shapes.append([(0,0), (1,0), (2,0), (3,0)])
shapes.append([(1,0), (0,1), (1,1), (2,1), (1,2)])
shapes.append([(2,2), (2,1), (0,0), (1,0), (2,0)])
shapes.append([(0,0), (0,1), (0,2), (0,3)])
shapes.append([(0,0), (1,0), (0,1), (1,1)])

colors = ["red", "green", "blue", "yellow", "magenta"] 

def get_shape(shape_nr, pos):
    shape = shapes[shape_nr]
    return [(t[0] + pos[0], t[1] + pos[1]) for t in shape]
    
def print_shapes():
    for shape in shapes:
        for j in range(4):
            for i in range(4):
                if (i,j) in shape:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

class Rock:
    def __init__(self, shape_nr: int = 0, position = (0,0)):
        self.tiles = get_shape(shape_nr, position)
        
    def move(self, vx, vy):
        self.tiles = [(t[0] + vx, t[1] + vy) for t in self.tiles]
        
    def push(self, wind_direction, tiles):
        if wind_direction == "<":
            speed = -1
        elif wind_direction == ">":
            speed = 1
        else:
            raise Exception("What")
        self.move(speed, 0)
        if self.collided(tiles):
            self.move(-speed, 0)

    def push_down(self, tiles):
        self.move(0, -1)
        if self.collided(tiles):
            self.move(0, 1)
            return False
        return True

    def collided(self, tiles):
        for pos in self.tiles:
            if pos in tiles:
                return True
            if pos[0] < 0 or pos[0] >= 7:
                return True
            if pos[1] < 0:
                return True
        return False

def print_grid(tiles, current_rock = Rock()):
    for row in range(max([t[1] for t in tiles]) + 5, max(-1, min([t[1] for t in tiles]) - 5), -1):
        print("{:>10}".format(row), end="")
        print("|", end="")
        for col in range(7):
            if (col, row) in tiles:
                print(colored("#", tiles[(col, row)]), end="")
            elif (col, row) in current_rock.tiles:
                print(".", end="")
            else:
                print(".", end="")
        print("|")
    print("          +-------+")

def run_iterations(iterations, movements):
    tiles = {}
    cutoff = 0
    cutoff_tiles = set()
    height_cutoff = 0
    m = 0
    max_height = 0

    for i in range(iterations):
        rock = Rock(i % len(shapes), [2, max_height + 3])
        while True:
            rock.push(movements[m], tiles)
            m = (m + 1) % len(movements)
            if not rock.push_down(tiles):
                color = colors[i % 5]
                for t in rock.tiles:
                    tiles[t] = color
                for t in rock.tiles:
                    cutoff_tiles.add(t[0])
                break
        max_height = max([x[1] + 1 for x in tiles])
        # if len(cutoff_tiles) == 7:
        #     tiles = dict([(t, v) for t,v in tiles.items() if t[1] >= cutoff])
        #     cutoff = max_height
        #     cutoff_tiles = set()
        # if i % 1000 == 0:
        #     print("           ", end="\r")
        #     print(i / iterations * 100, "%", end="\r")
    return max_height + height_cutoff, tiles
    
def drop_five(movements, m, tiles, max_height):
    for i in range(5):
        rock = Rock(i, [2, max_height + 3])
        while True:
            rock.push(movements[m], tiles)
            m = (m + 1) % len(movements)
            if not rock.push_down(tiles):
                color = colors[i % 5]
                for t in rock.tiles:
                    tiles[t] = color
                break
        max_height = max([x[1] + 1 for x in tiles])
    return m, max_height
        
def find_repeat(movements):
    tiles = {}
    m = 0
    max_height = 0
    visited = {}

    for i in range(1, 360):
        m, max_height = drop_five(movements, m, tiles, max_height)

    for i in range(1, 100000000):
        m, max_height = drop_five(movements, m, tiles, max_height)
        if m in visited:
            nr_blocks = i * 5 - visited[m][1]
            height_diff = max_height - visited[m][0]
            start_block = visited[m][1] + 1
            print_grid(tiles)
            return nr_blocks, height_diff, start_block
        
        visited[m] = (max_height, i * 5 )


    return max_height, tiles

nr_of_rocks = 1000000000000
movements = open("17.txt").readline().strip()

nr_blocks, height_diff, start_block = find_repeat(movements)
blocks_left = nr_of_rocks - (start_block - 1)
nr_of_repeats = blocks_left // nr_blocks - 1
top_blocks_left = blocks_left % nr_blocks

repeating_height = nr_of_repeats * height_diff
height, tiles = run_iterations(start_block - 1 + nr_blocks + top_blocks_left, movements)
print("The height of the stack is", repeating_height + height)
