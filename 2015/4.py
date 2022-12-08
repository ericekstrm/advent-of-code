import hashlib

secret = "yzbqklnj"

i = 1
found = False
while not found:
    test = secret + str(i)
    h = hashlib.md5(test.encode('utf-8')).hexdigest()
    if h[:6] == "000000":
        print(i)
        found = True
    i = i + 1
