from math import gcd

n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

for i in range(len(b) - 1):
    for j in range(i + 1, len(b)):
        if gcd(b[i], b[j]) == 1:
            print(b[i], b[j])