

with open("1.in") as input_file:
    lines = input_file.readlines()

total = 0
for line in lines:
    first_digit = None
    last_digit = None

    for i in range(len(line)):
        if line[i].isnumeric():
            last_digit = line[i]
            
        if line[i:].startswith("one"):
            last_digit = "1"
        if line[i:].startswith("two"):
            last_digit = "2"
        if line[i:].startswith("three"):
            last_digit = "3"
        if line[i:].startswith("four"):
            last_digit = "4"
        if line[i:].startswith("five"):
            last_digit = "5"
        if line[i:].startswith("six"):
            last_digit = "6"
        if line[i:].startswith("seven"):
            last_digit = "7"
        if line[i:].startswith("eight"):
            last_digit = "8"
        if line[i:].startswith("nine"):
            last_digit = "9"
            
        if first_digit == None:
            first_digit = last_digit   
    total += int(first_digit + last_digit)
print(total)
