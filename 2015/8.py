import re

data = [line.strip() for line in open("8.txt")]

original = "".join(data)
cof = len(original)
print(original)

reduced = re.sub('\\\\\\\\', "q", original)
reduced = re.sub("\\\\x..", "q", reduced)
reduced = re.sub('\\\\"', "q", reduced)
reduced = re.sub("\"", "", reduced)
print(cof, " - ", len(reduced), " = ", cof - len(reduced))

# part 2

expanded = re.sub("[\\\\\"]", "qq", original)
print(expanded)
print(len(expanded) + 2 * len(data), " - ", cof, " = ", len(expanded) + 2 * len(data) - cof)
