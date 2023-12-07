from dataclasses import dataclass
import copy

@dataclass
class Interval:
    start : int
    stop : int

    def overlap(self, other):
        return (self.stop >= other.start and self.start <= other.stop)

    def split(self, at):
        left = Interval(self.start, min(self.stop, at))
        right = Interval(max(self.start, at + 1), self.stop)
        if at < self.start:
            left = None
        if at > self.stop:
            right = None
        return left, right
    
class Set(object):
    def __init__(self):
        self.l = []

    def __str__(self):
        return str(self.l)

    def add(self, interval : Interval):
        if not interval:
            return
        if interval.stop < interval.start:
            return
        self.l.append(interval)
        self.l.sort(key=lambda i : i.start);

    def combine(self, other):
        for interval in other.l:
            self.add(interval)
        self.reduce()

    def reduce(self):
        for i in reversed(range(len(self.l) - 1)):
            if self.l[i].stop + 1 >= self.l[i+1].start:
                self.l[i].stop = self.l[i+1].stop
                del self.l[i+1]

    def extract(self, interval: Interval):
        start = 0
        while start < len(self.l) and not interval.overlap(self.l[start]):
            start += 1
        stop = start
        while stop < len(self.l) and interval.overlap(self.l[stop]):
            stop += 1


        if start >= len(self.l):
            return []

        extracted = self.l[start:stop]
        self.l = self.l[:start] + self.l[stop:]

        # print("extracted:", extracted)

        left_over, extracted[0] = extracted[0].split(interval.start-1)
        extracted[-1], right_over = extracted[-1].split(interval.stop)

        # print("left:", left_over)
        # print("right:", right_over)
        # print("new extracted:", extracted)
        self.add(left_over)
        self.add(right_over)
        return extracted


@dataclass
class Mapping:
    start : int
    stop : int
    diff : int

def transform(s: Set, m: list):

    new_intervals = []
    
    m.sort(key=lambda x : x.start)
    for mapping in m:
        extracted = s.extract(Interval(mapping.start, mapping.stop))
        # print(extracted)
        for e in extracted:
            
            e.start += mapping.diff
            e.stop += mapping.diff
            new_intervals.append(e)

    for interval in new_intervals:
        s.add(interval)
    s.reduce()

def line_to_list(line):
    return [int(i) for i in line.strip().split(" ") if i.isnumeric()]

def build_mapping(input_file):
    m = []
    nums = []
    while True:
        nums = line_to_list(input_file.readline())
        if nums == []:
            break
        m.append(Mapping(nums[1], nums[1] + nums[2] - 1, nums[0] - nums[1]))
    input_file.readline()
    return m

# parse data
with open("5.in") as input_file:
    seeds = line_to_list(input_file.readline().split(":")[1])
    input_file.readline()
    input_file.readline()

    seed_to_soil = build_mapping(input_file)
    soil_to_fert = build_mapping(input_file)
    fert_to_water = build_mapping(input_file)
    water_to_light = build_mapping(input_file)
    light_to_temp = build_mapping(input_file)
    temp_to_humi = build_mapping(input_file)
    humi_to_location = build_mapping(input_file)

# locations = []

starting_set = Set()
for s, d in zip(seeds[::2], seeds[1::2]):
    starting_set.add(Interval(s, s+d-1))
        
transform(starting_set, seed_to_soil)
transform(starting_set, soil_to_fert)
transform(starting_set, fert_to_water)
transform(starting_set, water_to_light)
transform(starting_set, light_to_temp)
transform(starting_set, temp_to_humi)
transform(starting_set, humi_to_location)

print("lowest location:", starting_set.l[0].start)
