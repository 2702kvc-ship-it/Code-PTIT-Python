t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))[:m]
    max = -1002032238948920310942344298394
    maxi = 0
    for i in range(m):
        if a[i] > max:
            max = a[i]
            maxi = i
    a.insert(maxi, n)
    for i in a:
        if i < 0:
            print(i, end=' ')
    for i in a:
        if i >= 0:
            print(i, end=' ')
    print()
            