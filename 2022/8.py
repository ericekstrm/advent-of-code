def is_tree_visible(grid, c, r):
    current_tree_height = grid[r][c]

    #go west
    highest = True
    for i in range(c - 1,-1, -1):
        if grid[r][i] >= current_tree_height:
            highest = False
    if highest:
        return True

    #go east
    highest = True
    for i in range(c + 1,cols, 1):
        if grid[r][i] >= current_tree_height:
            highest = False
    if highest:
        return True

    #go north
    highest = True
    for i in range(r - 1,-1, -1):
        if grid[i][c] >= current_tree_height:
            highest = False
    if highest:
        return True

    #go south
    highest = True
    for i in range(r + 1,rows, 1):
        if grid[i][c] >= current_tree_height:
            highest = False
    if highest:
        return True
    return False

data = open("8.txt")

grid = [line.strip() for line in data]

# Part 1
cols = len(grid[0])
rows = len(grid)   
result = 0
for c in range(1, cols - 1):
    for r in range(1, rows - 1):
        if is_tree_visible(grid, c, r):
            result += 1

circumference = cols * 2 + rows * 2 - 4
print(result + circumference)

# Part 2

def scenic_score(grid, c, r):
    current_tree_height = grid[r][c]

    #go west
    west_score = 0
    i = c - 1
    while i >= 0:
        west_score += 1
        if grid[r][i] >= current_tree_height:
            break
        i -= 1

    # go east
    east_score = 0
    i = c + 1
    while i < cols:
        east_score += 1
        if grid[r][i] >= current_tree_height:
            break
        i += 1

    # go north
    north_score = 0
    i = r - 1
    while i >= 0:
        north_score += 1
        if grid[i][c] >= current_tree_height:
            break
        i -= 1

    # go south
    south_score = 0
    i = r + 1
    while i < rows:
        south_score += 1
        if grid[i][c] >= current_tree_height:
            break
        i += 1

    return west_score * east_score * north_score * south_score

highest_score = 0
for c in range(0, cols):
    for r in range(0, rows):
        score = scenic_score(grid, c, r)
        if score > highest_score:
            highest_score = score
print(highest_score)
