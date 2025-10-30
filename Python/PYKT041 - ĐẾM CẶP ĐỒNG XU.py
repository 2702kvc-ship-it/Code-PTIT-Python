from math import *

def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)

t = int(input())
a = [[] * t for _ in range(t)]

for i in range(t):
    s = input()
    for j in s:
        a[i].append(j)

tong = 0

for i in range(t):
    cnt = a[i].count('C')
    if cnt < 2:
        continue
    tong += giaithua(cnt) // (giaithua(2) * giaithua(cnt - 2))
    cnt2 = 0
    for j in range(t):
        if a[j][i] == 'C':
            cnt2 += 1
    if cnt2 < 2:
        continue
    tong += giaithua(cnt2) // (giaithua(2) * giaithua(cnt2 - 2)) 

print(tong)