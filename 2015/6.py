import pprint

data = open("6.txt")

grid = []
for row in range(1000):
    grid.append([])

for row in grid:
   for col in range(1000):
       row.append(0)

for line in data:
    parts = line.split(" ")
    if line[0:4] == "turn":
        instruction = " ".join(parts[0:2])
    
        startpos = [int(x) for x in parts[2].split(",")]
        endpos =  [int(x) for x in parts[4].split(",")]
    else:
        instruction = "toggle"
        
        startpos = [int(x) for x in parts[1].split(",")]
        endpos =  [int(x) for x in parts[3].split(",")]

    for i in range(startpos[0], endpos[0]+1):
        for j in range(startpos[1], endpos[1]+1):
            
            if instruction == "toggle":
                grid[i][j] = grid[i][j] + 2

            if instruction == "turn on":
                grid[i][j] += 1 

            if instruction == "turn off":
                grid[i][j] -= 1
                if (grid[i][j] < 0):
                    grid[i][j] = 0
count = 0
for row in grid:
    for light in row:
        count += light
print(count)
