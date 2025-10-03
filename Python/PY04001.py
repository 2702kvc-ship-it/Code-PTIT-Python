import math

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(float, input().split())
    d = math.hypot(x1 - x2, y1 - y2)
    print(f"{d:.4f}")
