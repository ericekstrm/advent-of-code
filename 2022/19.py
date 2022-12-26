import time
start = time.time()

total_minutes = 32
resources = ["geode", "ore", "clay", "obsidian"]

def create_blueprint(blueprint_string: str):
    if blueprint_string == "":
        return None
    blueprint_string = blueprint_string.split(":")[1]
    blueprint_parts = blueprint_string[:-1].split(".")
    blueprint = {}
    for part in blueprint_parts:
        part = part.split()
        robot_type = part[1]
        costs = {}
        for c in " ".join(part[4:]).split(" and "):
            costs[c.split()[1]] = int(c.split()[0])
        blueprint[robot_type] = costs
    return blueprint

class Factory:

    def __init__(self, blueprint : str):
        self.blueprint = create_blueprint(blueprint)
        self.resources = {"ore":0, "clay":0, "obsidian":0, "geode":0}
        self.robots = {"ore":1, "clay":0, "obsidian":0, "geode":0}

    def mine(self):
        for res in self.resources:
            self.resources[res] += self.robots[res]

    def can_buy_robot(self, robot: str):
        robot_cost = self.blueprint[robot]
        for resource, cost in robot_cost.items():
            if self.resources[resource] < cost:
                return False
        return True
    
    def buy_robot(self, robot: str):
        self.mine()
        robot_cost = self.blueprint[robot]
        for resource, cost in robot_cost.items():
            self.resources[resource] -= cost
        self.robots[robot] += 1

    def clone(self):
        f = Factory("")
        f.blueprint = self.blueprint.copy()
        f.resources = self.resources.copy()
        f.robots = self.robots.copy()
        return f

    def max_needed(self, resource:str):
        if resource == "geode":
            return 999999999
        max_res = 0
        for robot_cost in self.blueprint.values():
            if resource in robot_cost:
                max_res = max(max_res, robot_cost[resource])
        return max_res

most_geodes = 0
def dfs(f: Factory, robot_to_buy, curr_minute: int):
    global most_geodes

    # is it even worth continuing?
    time_left = total_minutes - curr_minute + 1
    if f.resources["geode"] + time_left * f.robots["geode"] + (time_left * (time_left + 1) // 2) <= most_geodes:
        return 0
    
    while not f.can_buy_robot(robot_to_buy):
        f.mine()
        curr_minute += 1
        if curr_minute > total_minutes:
            return f.resources["geode"]

    f.buy_robot(robot_to_buy)
    curr_minute += 1
    if curr_minute > total_minutes:
        return f.resources["geode"]

    possible_robots = set([res for res in resources if f.robots[res] < f.max_needed(res)])
    try:
        # Not really changing the runtime :(
        if f.robots["obsidian"] == 0:
            possible_robots.remove("geode")
            if f.robots["clay"] == 0:
                possible_robots.remove("obsidian")
    except:
        pass
        
    max_geode = 0
    for r in possible_robots:
        geodes = dfs(f.clone(), r, curr_minute)
        max_geode = max(max_geode, geodes)
    most_geodes = max_geode
    return max_geode
    
def find_max_geodes(f: Factory):
    global most_geodes
    most_geodes = 0
    max_geodes = 0
    for r in ["ore", "clay"]:
        max_geodes = max(max_geodes, dfs(f.clone(), r, 1))
    return max_geodes

# f = Factory("Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.")
# f = Factory("Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.")

# print(find_max_geodes(f))

data = [line.strip() for line in open("19.txt")]

quality_level = 1
for i in range(3):
    print("Blueprint nr", i, end="\r")
    quality_level *= find_max_geodes(Factory(data[i]))
print()
print("Quality Level:", quality_level)

end = time.time()
print("Runtime was {:.2f}s".format(end - start))
