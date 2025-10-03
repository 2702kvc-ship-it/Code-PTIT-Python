from math import *
import sys

a, b, c = map(str, input().split())
a = float(a)
b = float(b)
if a <= 0 or b <= 0 or not a.is_integer() or not b.is_integer():
    print('INVALID')
    sys.exit()

print(int((a + b) * 2), int(a * b), c.title())

