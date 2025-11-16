index = []

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

min_value = 100001
max_value = -1
flag = False

for i in range(n):
    for j in range(m):
        min_value = min(min_value, a[i][j])
        max_value = max(max_value, a[i][j])

k = max_value - min_value
for i in range(n):
    for j in range(m):
        if a[i][j] == k:
            flag = True
            index.append([i, j])

if not flag:
    print("NOT FOUND")
else:
    print(k)
    for i, j in index:
        print(f"Vi tri [{i}][{j}]")