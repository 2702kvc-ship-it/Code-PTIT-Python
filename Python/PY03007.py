import sys
import re

s = sys.stdin.read().strip()
check = re.split(r'[.!?]+', s)

for i in check:
    i = i.strip()
    if i:
        i = i.lower().capitalize()
        x = i.split()
        for _ in x:
            print(_, end=' ')
        print()
