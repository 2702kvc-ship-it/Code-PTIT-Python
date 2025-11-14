import sys

data = sys.stdin.read().strip().split()
idx = 1

for _ in range(int(data[0])):
    s = data[idx]
    n = data[idx + 1]
    idx += 2
    i = 0
    cnt = 0
    while i + len(n) - 1 < len(s):
        if s[i: i + len(n)] == n:
            cnt += 1
            i += len(n)
        else:
            i += 1
    print(cnt)