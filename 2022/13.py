from functools import cmp_to_key

verbose = False
def compare(first, second, indentation):

    for i in range(min(len(first), len(second))):
        left = first[i]
        right = second[i]
    
        if verbose:
            print("{:>{i}}".format("", i=indentation), end="")
            print("- Compare", left, "vs", right)
        if type(left) == int and type(right) == list:
            left = [left]
            if verbose:
                print("{:>{i}}".format("", i=indentation), end="")
                print("- Mixing types; convert left to [{i}] and retry comparison".format(i=left))
                
        if type(left) == list and type(right) == int:
            right = [right]
            if verbose:
                print("{:>{i}}".format("", i=indentation), end="")
                print("- Mixing types; convert right to [{i}] and retry comparison".format(i=right))

        if type(left) == int and type(right) == int:
            if left < right:
                return 1
            elif left > right:
                return -1
        if type(left) == list and type(right) == list:
            comp = compare(left, right, indentation + 2)
            if comp != 0:
                return comp

    if len(first) < len(second):
        if verbose:
            print("{:>{i}}".format("", i=indentation), end="")
            print("- Left side ran out of items")
        return 1
    if len(first) > len(second):
        if verbose:
            print("{:>{i}}".format("", i=indentation), end="")
            print("- Right side ran out of items")
        return -1
        
    return 0

def sort_packets(packets):
    sorted_packets = sorted(packets, key=cmp_to_key(lambda x, y: compare(x, y, 2)), reverse=True)
    return sorted_packets

data = [l.strip() for l in open("13.txt")]

packet_pairs = []
for i in range(0,len(data), 3):
    packet_pairs.append((eval(data[i]), eval(data[i + 1])))

correct_pairs = []
i = 0
for pair in packet_pairs:
    first = pair[0]
    second = pair[1]

    i += 1
    if verbose:
        print("== Pair", i, "==")
        print("- Compare", first, "vs", second)
    result = compare(first, second, 2)
    if verbose:
        print("The results are in the", result, "order")
        print("")
    if result == 1:
        correct_pairs.append(i)
print("The sum of correct pairs indices is", sum(correct_pairs))

packets = [eval(l.strip()) for l in open("13.txt") if l.strip() != ""]
packets.append([[2]])
packets.append([[6]])
sorted_packets = sort_packets(packets)

mi = 0
ma = 0
for i in range(len(sorted_packets)):
    if sorted_packets[i] == [[2]]:
        mi = i + 1
    if sorted_packets[i] == [[6]]:
        ma = i + 1

print("The decoder key is", mi * ma)
