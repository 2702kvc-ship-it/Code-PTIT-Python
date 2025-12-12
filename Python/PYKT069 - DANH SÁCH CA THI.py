with open('CATHI.in', 'r') as f:
    l = f.readlines()

ds = []
idx = 1
j = 1
for i in range(int(l[0])):
    ma = f"C{j:03d}"
    ds.append([ma, l[idx].strip(), l[idx + 1].strip(), l[idx + 2].strip()])
    idx += 3
    j += 1

ds.sort(key=lambda x: (x[1][6:] + x[1][3:5] + x[1][0:2], x[2][:2] + x[2][3:], x[0]))

for d in ds:
    print(*d)