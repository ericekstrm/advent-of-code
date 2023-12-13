def flip(l):
    return ["".join(x) for x in list(zip(*l))]

def find_symmetry(l):
    for i in range(1, len(l)):
        dist = min(i, len(l) - i)
        left = l[i-dist:i]
        right = l[i:i+dist]

        smudges = 0
        for x, y in zip("".join(left), "".join(right[::-1])):
            if x != y:
                smudges += 1
        if smudges == 1:
            return i
    return 0

with open("13.in") as input_file:
    contents = input_file.read()
    contents = contents.split("\n\n")
    patterns = [s.strip().split("\n") for s in contents]

total = 0
for pattern in patterns:
    total += 100 * find_symmetry(pattern)
    total += find_symmetry(flip(pattern))
print(total)

