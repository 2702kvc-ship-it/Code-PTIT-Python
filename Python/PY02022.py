from collections import Counter
from math import *
def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))
x = Counter(a)
for so, xh in x.items():
    if snt(so):
        print(so, xh)
