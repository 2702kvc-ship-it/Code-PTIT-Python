from math import gcd
import sys

data = sys.stdin.read().strip().split()
idx = 1

for _ in range(int(data[0])):
    n, k = int(data[idx]), int(data[idx + 1])
    check = False
    a = list(map(int, data[idx + 2: idx + 2 + n]))
    idx += 2 + n
    smin = 10 ** 9
    for i in range(len(a)):
        h = a[i]
        if h == k:
            check = True
            smin = 1
            break
        for j in range(i + 1, len(a)):
            h = gcd(h, a[j])
            if h == k:
                check = True
                smin = min(smin, j - i + 1)
                break
        
    if check:
        print(smin)
    else:
        print(-1)



