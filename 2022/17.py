shapes = []
shapes.append([(0,0), (1,0), (2,0), (3,0)])
shapes.append([(1,0), (0,1), (1,1), (2,1), (1,2)])
shapes.append([(2,2), (2,1), (0,0), (1,0), (2,0)])
shapes.append([(0,0), (0,1), (0,2), (0,3)])
shapes.append([(0,0), (1,0), (0,1), (1,1)])
max_height = 0

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

def print_grid(current_rock, tiles):
    for row in range(max_height + 10, -1, -1):
        print("|", end="")
        for col in range(7):
            if (col, row) in tiles:
                print("#", end="")
            elif (col, row) in current_rock.tiles:
                print("@", end="")
            else:
                print(".", end="")
        print("|")
    print("+-------+")

class Rock:
    def __init__(self, shape_nr: int, position):
        self.tiles = get_shape(shape_nr, position)
        
    def move(self, vx, vy):
        self.tiles = [(t[0] + vx, t[1] + vy) for t in self.tiles]
        
    def push(self, wind_direction):
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
print("================")
nr_of_rocks = 100
tiles = set()
movements = open("17.txt").readline().strip()
m = 0

cutoff = 0
cutoff_tiles = set()
height_cutoff = 0

for i in range(nr_of_rocks):
    rock = Rock(i % len(shapes), [2, max_height + 3])
    print("New rock begin falling:")
    print_grid(rock, tiles)
    while True:
        rock.push(movements[m])
        m = (m + 1) % len(movements)
        # print("Rock is pushed", "left" if movements[m-1] == "<" else "right")
        # print_grid(rock, tiles)
        if not rock.push_down(tiles):
            tiles.update(rock.tiles)
            for t in rock.tiles:
                cutoff_tiles.add(t[0])
            break
        # input("")
    max_height = max([x[1] + 1 for x in tiles])
    # if len(cutoff_tiles) == 7:
    #     tiles = set([t for t in tiles if t[1] >= cutoff])
    #     cutoff = max_height
    #     cutoff_tiles = set()
    # if i % 100000 == 0:
    #     print("           ", end="\r")
    #     print(i / 1000000000000 * 100, "%", end="\r")

print("The height if the stack is", max_height + height_cutoff)
