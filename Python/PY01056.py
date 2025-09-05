from math import *

def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    tong = 0
    for i in range(0, len(n), 2):
        if int(n[i]) % 2 != 0:
            return False
        tong += int(n[i])
    for i in range(1, len(n), 2):
        if int(n[i]) % 2 == 0:
            return False
        tong += int(n[i])
    if snt(tong):
        return True
    return False

for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")