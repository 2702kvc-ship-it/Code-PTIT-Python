from math import *

for _ in range(int(input())):
    s = input()
    if gcd(int(s), int(s[::-1])) == 1:
        print("YES")
    else:
        print("NO")