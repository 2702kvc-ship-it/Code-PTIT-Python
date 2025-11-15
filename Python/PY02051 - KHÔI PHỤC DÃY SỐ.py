n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

if n == 2:
    print(a[0][1] // 2, a[0][1] // 2)

else:
    A0 = (a[0][1] + a[0][2] - a[1][2]) // 2
    l = [0] * n
    l[0] = A0
    for i in range(1, n):
        l[i] = a[0][i] - A0
    print(*l)