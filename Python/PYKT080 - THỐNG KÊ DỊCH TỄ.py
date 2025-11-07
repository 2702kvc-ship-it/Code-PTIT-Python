import sys

data = sys.stdin.read().strip().split()
idx = 2

m, n = int(data[0]), int(data[1])
a = []

flag = [[0] * n for _ in range(m)]

for i in range(m):
    a.append(list(map(int, data[idx : idx + n])))
    idx += n

for i in range(m):
    for j in range(n):
        if a[i][j] == -1:
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == dj == 0:
                        continue
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                            flag[ni][nj] = 1 #troll vãi đái, đề ra 1 đằng test case 1 nẻo
res = 0
for i in range(m):
    for j in range(n):
        if flag[i][j] == 1:
            res += a[i][j]

print(res)