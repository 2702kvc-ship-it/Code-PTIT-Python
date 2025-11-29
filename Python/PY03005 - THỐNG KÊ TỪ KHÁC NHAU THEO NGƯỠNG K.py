import re
from collections import Counter

n, k = map(int, input().split())
s = ""
for _ in range(n):
    s += input() + " "

w = re.findall(r"\b\w+\b", s.lower())

count = Counter(w)
ds = []
for w, f in count.items():
    if f >= k:
        ds.append((w, f))

ds.sort(key=lambda x: (-x[1], x[0]))

for i in ds:
    print(*i)