lines = []

with open("4.in") as input_file:
    lines = input_file.readlines()

multiplier = [1] * len(lines)

for i in range(len(lines)):
    card_name, line = lines[i].split(":")
    answer, mynums = line.split("|")
    answer = set([int(s) for s in answer.split(" ") if s])
    mynums = set([int(s) for s in mynums.split(" ") if s])

    winning_numbers = len(answer.intersection(mynums))

    for m in range(i + 1, min(len(multiplier), i + 1 + winning_numbers)):
        multiplier[m] += multiplier[i]

print(sum(multiplier))
