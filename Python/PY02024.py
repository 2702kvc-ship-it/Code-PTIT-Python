import sys
input = sys.stdin.readline

def tichchuso(n):
    tich = 1
    for i in n:
        tich *= int(i)
    return tich

for _ in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key=lambda s: (tichchuso(s), int(s)))
    print(*a)
