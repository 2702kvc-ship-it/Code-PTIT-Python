def check(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    return False

from math import *

def sangnt(n):
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return s

k = sangnt(502)
t = int(input())
for _ in range(t):
    n = input()
    ck = True
    for i in range(len(n)):
        if check(int(n[i])):
            if not k[i]:
                ck = False
                break
        else:
            if k[i]:
                ck = False
                break
    if ck:
        print("YES")
    else:
        print("NO")