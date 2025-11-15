n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
up = 0
down = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif i < j:
            up += a[i][j]
        else:
            down += a[i][j]

chenhlech = abs(up - down)
if chenhlech <= k:
    print("YES")
else:
    print("NO")
print(chenhlech)
