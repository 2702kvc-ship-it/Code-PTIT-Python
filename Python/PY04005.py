from math import *
import sys

data = sys.stdin.read().split()
idx = 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
    def check(self, b, c):
        s = abs(self.x * (b.y - c.y) + b.x * (c.y - self.y) + c.x * (self.y - b.y))
        return s > 0

if __name__ == "__main__":
    for _ in range(int(data[0])):
        x1, y1, x2, y2, x3, y3 = map(float, data[idx:idx+6])
        idx += 6
        a = Point(x1, y1)
        b = Point(x2, y2)
        c = Point(x3, y3)
        if a.check(b, c):
            ab = a.distance(b)
            ac = a.distance(c)
            bc = b.distance(c)
            p = ab + ac + bc
            print(f"{p:.3f}")
        else:
            print("INVALID")