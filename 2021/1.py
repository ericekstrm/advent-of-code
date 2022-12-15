
data = [int(l) for l in open("1.txt")]

result = 0
for i in range(1, len(data)):
    d = sum(data[i:i+3])
    p = sum(data[i-1:i+2])
    if d > p:
        result += 1
    prev = d
print(result)
            
    
