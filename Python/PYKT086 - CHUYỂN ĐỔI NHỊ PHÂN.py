import string
import sys

with open('DATA.in', 'r') as f:
    data = f.read().strip().split()

ds = string.digits + string.ascii_uppercase

idx = 1

for _ in range(int(data[0])):
    coso = int(data[idx])
    nhiphan = data[idx + 1]
    h10 = int(nhiphan, 2)
    res = ''
    if h10 == 0:
        print(0)
        continue
    while h10 > 0:
        res = ds[h10 % coso] + res
        h10 //= coso
    print(res)
    idx += 2