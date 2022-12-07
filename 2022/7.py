# Returns the size of a given directory
def sizeof(m):
    s = 0
    for d in m:
        if type(m[d]) == int:
            s += m[d]
        else:
            s += sizeof(m[d])
    return s

# Splits a line into a command and its argument
def split_command(line):
    command = ""
    argument = ""
    if "$" not in line:
        raise Exception("Not a command!")
    line = line[2:]
    if line[:2] == "ls":
        command = "ls"
    else:
        split_point = line.find(" ")
        command = line[:split_point]
        argument = line[split_point+1:]
    return command, argument

# Reads the ls command and returns the resulting file structure and the list of commands not used
def read_ls(commands):
    files = {}

    if "$ ls" not in commands[0]:
        raise Exception("Commands was not ls when expected ls")
    commands.pop(0)

    while commands:
        line = commands[0]
        
        if "$" in line:
            break
        commands.pop(0)
        
        l1, l2 = line.split()
        if l1 == "dir":
            files[l2] = {}
        else:
            files[l2] = int(l1)

    return files, commands

def build_tree(commands):
    files = {}

    while commands:
        command, argument = split_command(commands[0])
        if command == "ls":
            files, commands = read_ls(commands)
            continue
        if command == "cd":
            commands.pop(0)
            if argument == "..":
                break
            files[argument], commands = build_tree(commands)
            continue
            
    return files, commands
        
def directory_sizes(files):
    current_dir_size = 0
    directories = []
    
    for key, val in files.items():
        if type(val) == int:
            current_dir_size += val
        elif type(val) == dict:
            current_dir_size += sizeof(val)
    directories.append(current_dir_size)

    for key, val in files.items():
        if type(val) == dict:
            directories += directory_sizes(val)

    return directories
            
max_storage = 70000000
needed_storage = 30000000
cutoff = 100000

data = open("7.txt")

commands = [line.strip() for line in data]
commands.pop(0) # first commands is always "cd /" which is where we are anyways

files, commands = build_tree(commands)
directories = directory_sizes(files)

# Part 1
result = 0
for val in directories:
    if val <= cutoff:
        result += val
print(result)

# Part 2
directories.sort()
used_space = directories[-1]
needed_space = needed_storage - (max_storage - used_space)

result = used_space
for val in directories:
    if val >= needed_space and val < result:
        result = val
print(result)
