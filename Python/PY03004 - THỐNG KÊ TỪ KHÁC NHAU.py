import re
from collections import Counter

n = int(input())
s = ""
for _ in range(n):
    s += input() + " "

words = re.findall(r'\b\w+\b', s.lower())
count = Counter(words)

count = dict(sorted(count.items(), key=lambda x: (-x[1], x[0])))

for w, f in count.items():
    print(f"{w} {f}")
