
times = []
distances = []

with open("6.in") as input_file:
    times = [s for s in input_file.readline().split(":")[1].split(" ") if s]
    distances = [s for s in input_file.readline().split(":")[1].split(" ") if s]

    times = [int("".join(times))]
    distances = [int("".join(distances))]
    
    print(times)
    print(distances)

    total = 1

    for race in range(len(times)):
        race_total = 0

        for charge_time in range(times[race]):
            distance_traveled = charge_time * (times[race] - charge_time)

            if distance_traveled > distances[race]:
                race_total += 1
        total *= race_total
        print("Total:", total)

