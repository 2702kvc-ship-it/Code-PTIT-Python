s = input()
k = int(input())
res = []
if len(s) % 2 == 0:
    for i in range(0, len(s), 2):
        tmp = '' + s[i] + s[i + 1]
        res.append(int(tmp))
else:
    for i in range(0, len(s) - 1, 2):
        tmp = '' + s[i] + s[i + 1]
        res.append(int(tmp))

sort = []

from collections import Counter
count = Counter(res)

for x, y in count.items():
    if y >= k:
        sort.append([x, y])

sort = sorted(sort, key=lambda x: x[0])

if len(sort) == 0:
    print("NOT FOUND")
    import sys
    sys.exit()
for x, y in sort:
    print(x, y)