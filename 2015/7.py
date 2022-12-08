from ctypes import c_uint16

wire_values = {}

def handle_connection(connection : str):
    
    w1 = 0
    w2 = 0
    
    inwires, outwire = [x.strip() for x in connection.split("->")]
    if "AND" in inwires:
        w1, w2 = [x.strip() for x in inwires.split("AND")]
    elif "OR" in inwires:
        w1, w2 = [x.strip() for x in inwires.split("OR")]
    elif "RSHIFT" in inwires:
        w1, w2 = [x.strip() for x in inwires.split("RSHIFT")]
    elif "LSHIFT" in inwires:
        w1, w2 = [x.strip() for x in inwires.split("LSHIFT")]
    elif "NOT" in inwires:
        w2 = inwires.split("NOT")[1].strip() 
    else:
        w1 = inwires
            
    if w1 in wire_values:
        w1 = wire_values[w1]
    elif type(w1) == str and w1.isnumeric():
        w1 = int(w1)
    if w2 in wire_values:
        w2 = wire_values[w2]
    elif type(w2) == str and w2.isnumeric():
        w2 = int(w2)
        
    if type(w1) != int or type(w2) != int:
        return False
    
    if "AND" in inwires:
        wire_values[outwire] = w1 & w2
    elif "OR" in inwires:
        wire_values[outwire] = w1 | w2
    elif "RSHIFT" in inwires:
        wire_values[outwire] = w1 >> w2
    elif "LSHIFT" in inwires:
        wire_values[outwire] = w1 << w2
    elif "NOT" in inwires:
        wire_values[outwire] = c_uint16(~w2).value
    else:
        wire_values[outwire] = w1

    return True

    
data = open("7.txt")

lines = [line for line in data]

while len(lines) > 0:
    lines = [line for line in lines if not handle_connection(line)]
    print(len(lines))
    
print(wire_values)            
