import sys

data = sys.stdin.read().strip().split()

idx = 1

n = int(data[0])
a = list(map(int, data[idx:idx + n]))

i = 1
flag = False
while i < max(a):
    if i not in a:
        print(i)
        flag = True
    i += 1

if not flag:
    print("Excellent!")