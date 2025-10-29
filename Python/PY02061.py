for _ in range(int(input())):
    m, n = map(int, input().split())
    a = [[0] * n for _ in range(m)]
    for i in range(m):
        a[i] = list(map(int, input().split()))[:n]
    b = [[0] * 3 for _ in range(3)]
    for i in range(3):
        b[i] = list(map(int, input().split()))[:3]
    if m < 3 or n < 3:
        print("-1")
        continue
    res = 0
    for i in range(m - 2):
        for j in range(n - 2):
            res += (a[i][j] * b[0][0] + a[i][j + 1] * b[0][1] + a[i][j + 2] * b[0][2]
                    + a[i + 1][j] * b[1][0] + a[i + 1][j + 1] * b[1][1] + a[i + 1][j + 2] * b[1][2]
                    + a[i + 2][j] * b[2][0] + a[i + 2][j + 1] * b[2][1] + a[i + 2][j + 2] * b[2][2])
    print(res)