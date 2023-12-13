



def flip(l):
    return list(zip(*l))
    


def convert_to_ints(pattern):
    binarys = []
    for line in pattern:
        binarys.append(int("".join(["1" if c == "#" else "0" for c in line]), 2))
    return binarys



with open("13.in") as input_file:
    contents = input_file.read()
    contents = contents.split("\n\n")

    patterns = [s.strip().split("\n") for s in contents]
    pattern = patterns[0]
    print(pattern)
    print(convert_to_ints(pattern))
    pattern = flip(pattern)
    print(convert_to_ints(pattern))
    
