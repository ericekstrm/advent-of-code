
data = open("1.txt")

data = [int(l) for l in data]

result = 0
prev = sum(data[0:3])
for i in range(1, len(data)-3):
    d = sum(data[i:i+3])
    if d > prev:
        result += 1
    prev = d
print(result)
            
    
