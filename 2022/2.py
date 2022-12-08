
data = open("2.txt")
tab = {"A X":4, "A Z":3, "A Y":8, "C X":7, "C Z":6, "C Y":2, "B X":1, "B Z":9, "B Y":5}

result = 0
for line in data:
    line = line.strip()
    result += tab[line]
print(result)

tab2 = {"A X":3, "A Z":8, "A Y":4, "C X":2, "C Z":7, "C Y":6, "B X":1, "B Z":9, "B Y":5}

data = open("2.txt")
result = 0
for line in data:
    line = line.strip()
    result += tab2[line]
print(result)
