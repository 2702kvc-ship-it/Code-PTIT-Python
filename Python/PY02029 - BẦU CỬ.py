n, m = map(int, input().split())
a = list(map(int, input().split()))
tmp = {}

for i in a:
    if tmp.get(i) is None:
        tmp[i] = 1
    else:
        tmp[i] += 1

a = sorted(tmp, key=lambda x: (-tmp[x], x))
amax = tmp[a[0]]
while len(a) > 0 and tmp[a[0]] == amax:
    a.pop(0)

if len(a) == 0:
    print("NONE")
else:
    print(a[0])
