
class Elem:
    def __init__(self, char):
        self.char = char
        self.steps_away = None

lines = [l.strip() for l in open("12.txt")]

grid = {}

height = len(lines)
width = len(lines[0])

print("Size of map:", width, height)

for y, line in zip(range(len(lines))[::-1],lines[::-1]):
    for x, char in zip(range(width), line):
        grid[(x, y)] = Elem(char)
        if char == "E":
            end_pos = (x, y)
            grid[(x, y)] = Elem("z")
        if char == "S":
            start_pos = (x, y)
print("Start position is", start_pos, "and end position is", end_pos)

queue = []

queue.append(end_pos)
grid[end_pos].steps_away = 0 

while len(queue) != 0:
    current_position = queue[0]
    x = current_position[0]
    y = current_position[1]
    queue.pop(0)

    steps_away = grid[current_position].steps_away 
    current_char = grid[current_position].char

        
    # print("Searching candidate", current_position, "with height", current_char, "and value", steps_away)
    
    candidate_positions = [(x+1, y), (x-1, y), (x, y + 1), (x, y - 1)]

    for candidate in candidate_positions:
        if candidate[0] < width and candidate[0] >= 0 and candidate[1] < height and candidate[1] >= 0:
            if grid[candidate].char == "S" and ord(grid[current_position].char) < 99:
                print("The 'S' is", steps_away + 1, "steps away")
            if grid[candidate].char == "a" and ord(grid[current_position].char) < 99:
                print("There is an 'a' at", steps_away + 1, "steps at position", candidate)

            if grid[candidate].steps_away == None and ord(current_char) - ord(grid[candidate].char) <= 1:
                grid[candidate].steps_away = steps_away + 1
                queue.append(candidate)
                
