from math import *

def prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def emirp(n):
    n = str(n)
    if n != n[::-1]:
        if prime(int(n)) and prime(int(n[::-1])):
            return True
    return False


for _ in range(int(input())):
    n = int(input())
    res = []
    for i in range(12, n):
        k = int(str(i)[::-1])
        if emirp(i) and k < n and i not in res and k not in res:
            res.append(i)
            res.append(k)
    
    for i in res:
        print(i, end= ' ')
    print()
