from collections import deque

escapable_positions = {}
def escape(coord: tuple, data):
    que = deque([coord])
    visited_positions = set() 
    escapable = False
    
    while len(que) != 0:
        current_coord = que.popleft()
        visited_positions.add(current_coord)
        if current_coord in escapable_positions:
            escapable = escapable_positions[current_coord]
            break
            
        if max(current_coord) > 21 or min(current_coord) < 0:
            escapable = True
            break
            
        for n in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]:
                new_coord = tuple([sum(x) for x in zip(current_coord, n)])
                if new_coord not in visited_positions and new_coord not in que and new_coord not in data:
                    que.append(new_coord)
        
    for pos in visited_positions:
        escapable_positions[pos] = escapable
    return escapable

data = [tuple([int(x) for x in l.strip().split(",")]) for l in open("18.txt")]

count = 0
for c in data:
    for n in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]:
        new_coord = tuple([sum(x) for x in zip(c, n)])
        if new_coord not in data and escape(new_coord, data):
            count += 1

print(count)
