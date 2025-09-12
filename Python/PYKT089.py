import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.read().split()))
chan = []
le = []
for i in a:
    if i % 2 == 0:
        chan.append(i)
    else:
        le.append(i)

chan.sort()
le.sort(reverse= True)

res = []
x, y = 0, 0
for i in a:
    if i % 2 == 0:
        res.append(chan[x])
        x += 1
    else:
        res.append(le[y])
        y += 1

print(*res, sep=" ")