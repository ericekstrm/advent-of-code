mapping = {
    "|": [(-1,  0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)]
}

# get the character in the graph at a specified position
def get(graph, pos):
    return graph[pos[0]][pos[1]]

# replace a character in the graph at a specified position
def setg(graph, pos, v):
    graph[pos[0]] = graph[pos[0]][:pos[1]] + v + graph[pos[0]][pos[1]+1:]

# sum two tuples element wise
def add(pos1, pos2):
    return tuple([sum(x) for x in zip(pos1, pos2)])

# Find the start position
def start_pos(graph):
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if graph[row][col] == "S":
                return (row, col)

# Calculate the two adjecent points of a given position
def get_adjecent(graph, pos):
    left_point, right_point = mapping[get(graph, pos)]
    return add(pos, left_point), add(pos, right_point)

# find the start position, replace it with its correct character and return one of the adjecent points
def resolve_start(graph):
    start = start_pos(graph)

    surrounding_pos = [(1,0), (-1, 0), (0, -1), (0,1)]
    adjecent_pos = []
    for p in surrounding_pos:
        left, right = get_adjecent(graph, add(start, p))
        pipe_shape = get(graph, p)
        if start == left or start == right:
            adjecent_pos.append(p)

    for k, v in mapping.items():
        if adjecent_pos[0] in v and adjecent_pos[1] in v:
            setg(graph, start, k)

    return start, add(start, adjecent_pos[0])
    
# Move one step along the loop
def step(graph, pos, prev_pos):
    left_path, right_path = get_adjecent(graph, pos)
    if left_path == prev_pos:
        return right_path, pos
    return left_path, pos

def count_line(graph, row, loop_parts):
    count = 0
    inside = False
    entered_from_above = False
    entered_from_below = False

    for i, c in enumerate(graph[row]):
        
        if (row, i) not in loop_parts:
            if inside:
                print("O", end="")
                count += 1
            else:
                print("I", end="")
            continue

        print(c, end="")

        if c == "-":
            continue

        if c == "|":
            inside = not inside

        if c in "F7":
            if entered_from_above:
                inside = not inside
                entered_from_above = False
            else:
                entered_from_below = not entered_from_below
                
        if c in "LJ":
            if entered_from_below:
                inside = not inside
                entered_from_below = False
            else:
                entered_from_above = not entered_from_above
    print("")
    return count

if __name__ == "__main__":
        
    with open("10.in") as input_file:
        graph = [s.strip() for s  in input_file.readlines() if s]

    start, pos = resolve_start(graph)
    prev_pos = start
    loop_parts = set(pos)

    steps = 1
    while pos != start:
        pos, prev_pos = step(graph, pos, prev_pos)
        loop_parts.add(pos)
        steps += 1

    total = 0
    for row in range(len(graph)):
        total += count_line(graph, row, loop_parts)

    print("The point at the far end is", steps // 2, "steps away")
    print("Total enclosed spaces:", total)
