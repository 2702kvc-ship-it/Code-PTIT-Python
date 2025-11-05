n, k = map(int, input().split())
dem = 0
from math import gcd
for i in range(10 ** (k - 1), 10 ** k):
    if gcd(i, n) == 1:
        dem += 1
        print(i, end=' ')
    if dem == 10:
        print()
        dem = 0