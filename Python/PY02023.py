import sys
input = sys.stdin.readline

def chuso(n):
    tong = 0
    for i in n:
        tong += int(i)
    return tong

def sapxep(n):
    return chuso(str(n)), n

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a, key=sapxep)
    print(*b)
