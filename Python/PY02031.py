from math import *
import sys
input = sys.stdin.readline

def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

m, n = map(int, input().split())
a = [0] * m
for i in range(m):
    a[i] = list(map(int, input().split()))
    for j in range(len(a[i])): 
        if snt(a[i][j]):
            a[i][j] = 1 
        else: 
            a[i][j] = 0
    
for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()