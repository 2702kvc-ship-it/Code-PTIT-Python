for _ in range(int(input())):
    m, n = map(int, input().split())
    a = [[0] * n for _ in range(m)]
    for i in range(m):
        a[i] = list(map(int, input().split()))

    b = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            b[j][i] = a[i][j]
    c = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(m):
        print(*c[i])