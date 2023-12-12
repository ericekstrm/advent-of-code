from functools import cache

@cache
def count_arrangements(line, stats, bracket_count = 0):

    count = 0
    bracket_done = False

    if bracket_count == stats[0]:
        stats = stats[1:]
        bracket_count = 0
        bracket_done = True

    # no more stats to read (only dots left in the line)
    if len(stats) == 0:
        if "#" in line:
            count = 0
        else:
            count = 1

    elif len(line) == 0:
        count = 0

    # first character is a dot. Ignore and move on to next
    elif line[0] == ".":

        if bracket_count != 0:
            count = 0
        else:
            count = count_arrangements(line[1:], stats)

    # first character is bracket
    elif line[0] == "#":

        if bracket_done:
            count = 0
        else:
            count = count_arrangements(line[1:], stats, bracket_count+1)

    # first character is '?'. expand both options
    elif line[0] == "?":
        if bracket_count == 0:
            count += count_arrangements("." + line[1:], stats, bracket_count)
        if not bracket_done:
            count += count_arrangements("#" + line[1:], stats, bracket_count)

    return count
    
total = 0    
with open("12.in") as input_file:
    lines = [s.strip() for s in input_file.readlines() if s]
    for line in lines:
        springs, stats = line.split(" ")
        stats = tuple([int(s) for s in stats.split(",")])

        # multiply by 5
        springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
        stats = stats * 5

        total += count_arrangements(springs, stats)
    
print("The total nr of arrangements was", total)
