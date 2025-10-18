from math import *
import sys

data = sys.stdin.read().strip().split()
idx = 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def check(self, b, c):
        s = abs(self.x * (b.y - c.y) + b.x * (c.y - self.y) + c.x * (self.y - b.y)) / 2
        return s > 0
    def distance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))


if __name__ == "__main__":
    t = int(data[0])
    for _ in range(t):
        x1, y1, x2, y2, x3, y3 = map(float, data[idx:idx + 6])
        idx += 6
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)
        if p1.check(p2, p3):
            ab = p1.distance(p2)
            bc = p2.distance(p3)
            ca = p1.distance(p3)
            p = (ab + bc + ca) / 2
            s = sqrt((p) * (p - ab) * (p - bc) * (p - ca))
            print(f"{s:.2f}")
        else:
            print("INVALID")