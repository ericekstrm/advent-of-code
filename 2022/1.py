
data = open("1.txt")

result = [0]
for line in data:
    line = line.strip()
    if line.isnumeric():
        result[-1] += int(line)
    else:
        result.append(0)

result.sort()
print(result[-1])
print(sum(result[-3:]))
