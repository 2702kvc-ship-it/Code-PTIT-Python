n = int(input())
a = []
for i in range(n):
    a.append(input())

def swap(xau1, xau2):
    if xau1 == xau2:
        return 0
    for i in range(len(xau1)):
        xau2 = xau2[1:] + xau2[0]
        if xau1 == xau2:
            return i + 1
    return -1

check = True
ans = 1e19
for i in range(n):
    res = 0
    for j in range(n):
        if i != j:
            if swap(a[i], a[j]) != -1:
                res += swap(a[i], a[j])
            else:
                check = False
                break
    if check:
        ans = min(ans, res)

if check:
    print(ans)
else:
    print(-1)