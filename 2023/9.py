from itertools import pairwise

def extrapolate(seq):
    if all([i == 0 for i in seq]):
        return seq + [0]

    diffs = [y - x for x, y in pairwise(seq)]
    diffs = extrapolate(diffs)

    return [seq[0] - diffs[0]] + seq + [seq[-1] + diffs[-1]]

with open("9.in") as input_file:
    lines = input_file.readlines()

total = 0
total_back = 0
for line in lines:
    sequence = [int(s) for s in line.strip().split(" ") if s]
    extended_sequence = extrapolate(sequence)
    total += extended_sequence[-1]
    total_back += extended_sequence[0]
    
print("The sum of the last values was", total)
print("The sum of the first values was", total_back)
