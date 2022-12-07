
def inside(r1, r2):
    if r1[0] <= r2[0] and r1[1] >= r2[1]:
        return True
    return False
        
def covering(r1, r2):
    if inside(r1, r2) or inside(r2, r1):
        return True
    return False
        
def intersecting_left(r1, r2):
    return  (r1[0] <= r2[0] and r1[1] >= r2[0])

def intersecting(r1, r2):
    return intersecting_left(r1, r2) or intersecting_left(r2, r1)

data = open("4.txt")

result = 0
for line in data:
    p1, p2 = line.split(",")
    r1 = [int(x) for x in p1.split("-")]
    r2 = [int(x) for x in p2.split("-")]
    print(r1, r2, covering(r1, r2))
    if covering(r1, r2): result += 1 
print("part 1:", result)

data = open("4.txt")
result = 0
for line in data:
    p1, p2 = line.split(",")
    r1 = [int(x) for x in p1.split("-")]
    r2 = [int(x) for x in p2.split("-")]
    print(r1, r2, intersecting(r1, r2))
    if intersecting(r1, r2): result += 1 
print("part 2:", result)
