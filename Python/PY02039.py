n = int(input())
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))[:n]

k = int(input())
tongtren = tongduoi = 0
for i in range(n):
    for j in range(n):
        if i < j:
            tongtren += a[i][j]
        elif i > j:
            tongduoi += a[i][j]

if abs(tongtren - tongduoi) <= k:
    print("YES")
else:
    print("NO")

print(abs(tongtren - tongduoi))