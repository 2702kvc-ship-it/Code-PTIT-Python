import re
from collections import Counter

def check(s):
    if s.isdigit():
        return False
    hehe = '0123456789'
    tmp = ''
    for i in s:
        if i not in hehe:
            tmp += i
    return tmp

n = int(input())
s = ""
for _ in range(n):
    s += input() + " "

w = re.findall(r"\b\w+\b", s.lower())

count = Counter(w)
ds = []
for w, f in count.items():
    flag = check(w)
    if flag:
        ds.append((flag, f))

ds.sort(key=lambda x: (-x[1], x[0]))

for i in ds:
    print(*i)