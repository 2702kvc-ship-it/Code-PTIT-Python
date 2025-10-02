from math import *

s = list(map(int, input().split()))[:2]
ucln = gcd(*s)
print(f"{int(s[0] / ucln)}/{int(s[1] / ucln)}")