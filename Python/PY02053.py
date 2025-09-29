n = int(input())
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))[:n]

k = int(input())
tongtren = tongduoi = 0

for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            tongtren += a[i][j]
        elif i + j > n - 1:
            tongduoi += a[i][j]
        else:
            continue

kc = abs(tongtren - tongduoi)
print('YES' if kc <= k else 'NO')
print(kc)