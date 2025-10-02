from math import *

a, b, c, d = map(int, input().split())
tmp = gcd(b, d)
mau = (b * d) // tmp
tu = a * (mau // b) + c * (mau // d)
print(f"{tu // gcd(tu, mau)}/{mau // gcd(tu, mau)}")