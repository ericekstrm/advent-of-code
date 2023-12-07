

with open("2.in") as input_file:
    lines = input_file.readlines()

def possible_game(line):
    min_red   = 0
    min_green = 0
    min_blue  = 0
    rounds = [s.strip() for s in line.split(";")]
    for r in rounds:
        sets = [s.strip() for s in r.split(",")]
        for s in sets:
            amount, color = s.split(" ")
            amount = int(amount)
            if color == "red":
                min_red = max(min_red, amount)
            if color == "green":
                min_green = max(min_green, amount)
            if color == "blue":
                min_blue = max(min_blue, amount)
    print(min_red, min_green, min_blue)
    return min_red, min_green, min_blue

id_sum = 0
        
for line in lines:
    game_id, line = line.split(":")
    print(game_id)
    min_red, min_blue, min_green = possible_game(line)
    id_sum += min_red * min_blue * min_green
print(id_sum)
