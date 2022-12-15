
data = open("3.txt")

size = 12
gamma = [0] * size
nr_numbers = 0

for line in data:
   nr_numbers += 1
   for i in range(len(line)):
       if line[i] == "1":
           print(i)
           gamma[i] += 1
print(gamma)
print(nr_numbers)

binary_string_gamma = ""
binary_string_epsilon = ""
for i in gamma:
    if i > nr_numbers / 2:
        binary_string_gamma += "1"
        binary_string_epsilon += "0"
    
    if i < nr_numbers / 2:
        binary_string_gamma += "0"
        binary_string_epsilon += "1"
print(int(binary_string_gamma, 2) * int(binary_string_epsilon, 2))
