def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n - 1)

n = int(input())
a = []
for i in range(n):
    a.append(input())

cnt = 0

for i in range(n):
    c = 0
    for j in range(n):
        if a[i][j] == 'C':
            c += 1
    cnt += giaithua(c) // (giaithua(2) * giaithua(c - 2)) if c >= 2 else 0

for i in range(n):
    c = 0
    for j in range(n):
        if a[j][i] == 'C':
            c += 1
    cnt += giaithua(c) // (giaithua(2) * giaithua(c - 2)) if c >= 2 else 0

print(cnt)