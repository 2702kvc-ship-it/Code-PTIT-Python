from math import *

def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    n = int(input())
    k = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            k += 1
    print("YES" if snt(k) else "NO")