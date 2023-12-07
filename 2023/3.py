
with open("3.in") as input_file:
    lines = [s.strip() for s in input_file.readlines()]

def contains_symbol(s):
    for c in s:
        if c not in "0123456789.":
            return True
    return False

def try_get(line, start, end):
    return line[max(0,start):min(len(line),end)]

def find_numbers():
    numbers = {}
    
    for row in range(len(lines)):
        potential_part = ""

        for col in range(len(lines[0])):
            val = lines[row][col]
        
            if val.isnumeric():
                potential_part += val

            elif potential_part != "":
                numbers[(row, col)] = potential_part
                potential_part = ""
                
        if potential_part != "":
            numbers[(row, col)] = potential_part

    return numbers

def is_part(row, col, size):
    line1 = ""
    line2 = try_get(lines[row], col - size - 1, col + 1)
    line3 = ""
    if row != 0:
        line1 = try_get(lines[row-1], col - size - 1, col + 1)
    if row < len(lines) - 1:
        line3 = try_get(lines[row+1], col - size - 1, col + 1)

    all_chars = line1 + line2 + line3
    return contains_symbol(all_chars)

def get_gears():
    gears = {}
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            val = lines[row][col]
            if val == "*":
                gears[(row, col)] = []
    return gears

    
numbers = find_numbers()

sums = 0
for k, v in numbers.items():
    if is_part(k[0], k[1], len(v)):
        sums += int(v)
print("Part sums:", sums)

gears = get_gears()

def adjecent_gear(row, col, size):
    gears = []
    for i in range(max(0,row-1), min(len(lines),row+2)):
        for j in range(max(0,col - size - 1), min(len(lines),col+1)):
            if lines[i][j] == "*":
                gears.append((i,j))
    return gears

for k, v in numbers.items():
    for gear in adjecent_gear(k[0], k[1], len(v)):
        gears[gear].append(int(v))

gear_ratios = 0
for v in gears.values():
    if len(v) == 2:
        gear_ratios += v[0] * v[1]

print("Gear ratios:", gear_ratios)
