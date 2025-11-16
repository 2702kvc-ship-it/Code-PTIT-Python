n, m = map(int, input().split())
a = [list(map(int, input().split()))[:m] for _ in range(n)]

if n > m:
    k = n - m
    for i in range(n):
        if k > 0:
            if i % 2 == 0:
                k -= 1
                continue
            else:
                print(*a[i])
        else:
            print(*a[i])

else:
    k = m - n
    row = []
    value = 1
    while k > 0:
        row.append(value)
        value += 2
        k -= 1
        
    for i in range(n):
        for j in range(m):
            if j in row:
                continue
            else:
                print(a[i][j], end=' ')
        print()