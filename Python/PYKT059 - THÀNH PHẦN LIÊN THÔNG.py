n, m, x = map(int, input().split())
ke = [[] for x in range(0, n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    ke[a].append(b)
    ke[b].append(a)

dinh, q = [0] * (n + 1), [x]
dinh[x] = 1
while len(q) > 0:
    u = q.pop()
    for i in ke[u]:
        if dinh[i] == 0:
            q.append(i)
            dinh[i] = 1
check = True
for i in range(1, n + 1):
    if dinh[i] == 0:
        check = False
        print(i)
if check:
    print(0)