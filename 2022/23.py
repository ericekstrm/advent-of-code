directions = [(0,-1), (0,1), (-1,0), (1,0)]

def add(a: tuple, b:tuple):
    return tuple([sum(x) for x in zip(a, b)])

class Nisse:
    def __init__(self, pos):
        self.pos = pos
        self.new_pos = (0,0)

    def move(self):
        self.pos = add(self.pos, self.new_pos)
        self.new_pos = (0,0)

def print_board(elfs):
    xcoord = [elf.pos[0] for elf in elfs]
    ycoord = [elf.pos[1] for elf in elfs]
    print("===============================")
    print("   ", end="")
    for col in range(min(xcoord), max(xcoord) + 1):
        if col < 0:
            print("-", end="")
        else:
            print(" ", end="")
    print("\n   ", end="")
    for col in range(min(xcoord), max(xcoord) + 1):
        print(abs(col) // 10, end="")
    print("\n   ", end="")
    for col in range(min(xcoord), max(xcoord) + 1):
        print(abs(col) % 10, end="")
    print()

    for row in range(min(ycoord), max(ycoord) + 1):
        print("{:>2}|".format(row), end="")
        for col in range(min(xcoord), max(xcoord) + 1):
            if (col, row) in [elf.pos for elf in elfs]:
                print("#", end="")
            else:
                print(".", end="")
        print()
        
    
def read_elfs():
    data = [x.strip() for x in open("23.txt")]
    elfs = []
    x = 0
    y = 0
    for line in data:
        for c in line:
            if c == "#":
                elfs.append(Nisse((x,y)))
            x += 1
        x = 0
        y += 1
    return elfs

def propose_moves(elfs):
    proposed_moves = {}
    for elf in elfs:

        # find adjacent elfs
        adjacent_elfs = []
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                new_pos = add(elf.pos, (x,y))
                if new_pos in [elf.pos for elf in elfs]:
                    adjacent_elfs.append((x,y))

        if len(adjacent_elfs) == 1:
            continue

        # Propose move
        for d in directions:
            v = [(d[0] + (i*abs(d[1])), d[1] + (i*abs(d[0])) ) for i in [-1,0,1]]
            if len([p for p in v if p in adjacent_elfs]) == 0:
                elf.new_pos = d 
                new_pos = add(elf.pos, elf.new_pos)
                if new_pos not in proposed_moves:
                    proposed_moves[new_pos] = 0
                proposed_moves[new_pos] += 1
                break
    return proposed_moves
                
def move(elfs, proposed_moves):
    for elf in elfs:
        if elf.new_pos != (0,0) and proposed_moves[add(elf.pos, elf.new_pos)] == 1:
            elf.move()
        else:
            elf.new_pos =(0,0)
    return elfs

def switch_dir():
    first_dir = directions[0]
    directions.pop(0)
    directions.append(first_dir)


def count_spaces(elfs):
    xcoord = [elf.pos[0] for elf in elfs]
    ycoord = [elf.pos[1] for elf in elfs]
    result = 0
    for row in range(min(ycoord), max(ycoord) + 1):
        for col in range(min(xcoord), max(xcoord) + 1):
            if (col, row) not in [elf.pos for elf in elfs]:
                result += 1
    return result

def one_round(elfs):
    # elfs = [Nisse((4,4)), Nisse((4,5)), Nisse((1,2)), Nisse((4,2)), Nisse((4,1))]
    proposed_moves = propose_moves(elfs)
    elfs = move(elfs, proposed_moves)
    # print_board(elfs)
    switch_dir()
    return elfs, len(proposed_moves)

elfs = read_elfs()
# print_board(elfs)

i = 1
while True:
    elfs, moved_elfs = one_round(elfs)
    if moved_elfs == 0:
        print("Done at", i)
        break
    print(i)
    i += 1
print(count_spaces(elfs))

