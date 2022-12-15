
data = open("2.txt")

h = 0
d = 0
aim = 0
for line in data:
    direction, length = line.split()
    if direction == "forward":
        h += int(length)
        d += int(length) * aim
    if direction == "up":
        aim -= int(length)
    if direction == "down":
        aim += int(length)
      
print(h * d)
