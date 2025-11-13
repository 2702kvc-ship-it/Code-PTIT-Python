from math import *

def sieve(n):
    primes = [False] * (n + 1)
    primes[0] = primes[1] = True
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i] == False:
            for j in range(i * i, n + 1, i):
                primes[j] = True
    return [i for i in range(2, n + 1) if primes[i] == False]


n = int(input())
k = sieve(int(sqrt(n)))
cnt = 0

for i in k:
    if i ** 8 <= n:
        cnt += 1

for i in range(len(k) - 1):
    for j in range(i + 1, len(k)):
        if k[i] ** 2 * k[j] ** 2 <= n:
            cnt += 1
        else:
            break

print(cnt)
