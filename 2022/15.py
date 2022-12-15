def manhatan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def within_sensor(sensor, beacon, p):
    beacon_dist = manhatan_dist(sensor, beacon)
    point_dist = manhatan_dist(sensor, p)
    return beacon_dist >= point_dist

def within_any_sensor(sensors, beacons, p):
    for sensor, beacon in zip(sensors, beacons):
        if within_sensor(sensor, beacon, p):
            return True
    return False

def get_bounds(sensors, beacons):

    minx, maxx = sensors[0][0], sensors[0][0]
    
    for s, b in zip(sensors, beacons):
        dist = manhatan_dist(s, b)
        minx = min(s[0] - dist, minx)
        maxx = max(s[0] + dist, maxx)
    return minx - 5, maxx + 5
    
def max_min_sensors(sensors):
    minx, miny, miny, maxy = 0,0,0,0

def print_map(sensors, beacons):
    for y in range(-10, 30):
        print("{:>3} ".format(y), end="")
        for x in range(-10, 30):
            if (x, y) in sensors:
                print("S", end="")
            elif (x,y) in beacons:
                print("B", end="")
            elif within_any_sensor(sensors, beacons, (x,y)):
                print("#", end="")
            else:
                print(".", end="")
        print()
                
def get_rand_points(sensors, beacons):
    h_under = set()
    h_over = set()
    v_under = set()
    v_over = set()
    for s, b in zip(sensors, beacons):
        dist = manhatan_dist(s, b)
        h = (s[0] + dist, s[1])
        v = (s[0] - dist, s[1])

        x, y = h[0], h[1] + 1
        for i in range(dist + 1):
            h_under.add((x,y))
            x -= 1
            y += 1

        x, y = h[0], h[1] - 1
        for i in range(dist + 1):
            h_over.add((x,y))
            x -= 1
            y -= 1

        x, y = v[0], v[1] + 1
        for i in range(dist + 1):
            v_under.add((x,y))
            x += 1
            y += 1
        x, y = v[0], v[1] - 1
        for i in range(dist + 1):
            v_over.add((x,y))
            x += 1
            y -= 1
    return h_under, h_over, v_under, v_over
            

data = [l.strip() for l in open("15.txt")]
sensors = []
beacons = []

for line in data:
    sensor, beacon = [x.strip() for x in line.split(":")]
    sx, sy = [int(x.strip()) for x in sensor.split(",")]
    bx, by = [int(x.strip()) for x in beacon.split(",")]
    sensors.append((sx,sy))
    beacons.append((bx, by))

the_row = 2000000
start, stop = get_bounds(sensors, beacons) 

print("Bounds", start, stop)
# print_map(sensors, beacons)

count = 0
for x in range(start, stop + 1):
    pos = (x, the_row)

    if pos not in beacons and within_any_sensor(sensors, beacons, pos):
        count += 1

print("Part 1:", count)

hu, ho, vu, vo = get_rand_points(sensors, beacons)
s1 = hu.intersection(ho)
s2 = ho.intersection(vo)
s3 = vo.intersection(vu)
s4 = vu.intersection(hu)
s = s1.union(s2, s3, s4)

for p in s:
    if p[0] >= 0 and p[0] <= 4000000 and p[1] >= 0 and p[1] <= 4000000:
        if not within_any_sensor(sensors, beacons, p):
            print("Part 2:", p, "->", p[0]*4000000+p[1])
