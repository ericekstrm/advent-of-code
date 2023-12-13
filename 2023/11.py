def flip(lines):
    return list(zip(*lines))
        
def add_space(lines):
    new_lines = []
    for line in lines:
        if "#" in line:
            new_lines.append(line)
        else:
            new_lines.append(line)
            new_lines.append(line)
    return new_lines

with open("11.in") as input_file:
    lines = [s.strip() for s in input_file.readlines()]

    empty_rows = [i for i, line in enumerate(lines) if "#" not in line]
    empty_cols = [i for i, line in enumerate(flip(lines)) if "#" not in line]
    
    points = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "#":
               points.append((col, row))

total = 0
for i, p1 in enumerate(points):
    for p2 in points[i+1:]:
        x1 = min(p1[0], p2[0]) 
        y1 = min(p1[1], p2[1]) 
        x2 = max(p1[0], p2[0]) 
        y2 = max(p1[1], p2[1]) 
        
        count_emptys = 0
        for x in empty_cols:
            if x in range(x1, x2):
                count_emptys += 1
        for y in empty_rows:
            if y in range(y1, y2):
                count_emptys += 1
        
        a = x2 - x1 + y2 - y1
        total += a + count_emptys * 1000000 - count_emptys
print("Sum of all manhattan distances was", total)
