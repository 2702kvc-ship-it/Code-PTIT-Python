ds = []

with open("CONTACT.in", "r") as f:
    data = f.readlines()
    for line in data:
        line = line.lower().strip()
        if line not in ds:
            ds.append(line)

ds.sort()
for i in ds:
    print(i)