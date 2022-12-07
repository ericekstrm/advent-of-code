
data = open("6.txt").readline()

distinct = 4
def unique(s):
    return len(s) == len(set(s))

for i in range(len(data)):
    if unique(data[i:i+distinct]):
        print(i + distinct)
        break
