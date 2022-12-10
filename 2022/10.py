
data = open("10.txt")

signal_strengths = []
X = 1
cycle = 1


for line in data:
    if (cycle - 20) % 40 == 0:
        signal_strengths.append(X * cycle)
    if "noop" in line:
        cycle += 1
        continue
    elif "addx" in line:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            signal_strengths.append(X * cycle)
        cycle += 1
        X += int(line.split()[1])
        
print("part 1 :", sum(signal_strengths))

data.close()
data = open("10.txt")

X = 1
add_value = 0
for y in range(6):
    for x in range(40):
        if abs(X - x) < 2:
            print("#", end="")
        else:
            print(".", end="")

        if add_value != 0:
            X += add_value
            add_value = 0
        else:
            line = data.readline() 
            if "noop" not in line:
                add_value = int(line.split()[1])

    print()
        
