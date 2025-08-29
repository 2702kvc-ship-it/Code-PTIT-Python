from math import *

def prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    s = input()
    tmp = ""
    for i in range(len(s) - 4, len(s)):
        tmp += s[i]
    if prime(int(tmp)):
        print("YES")
    else:
        print("NO")