a = list(map(int, input().split()))[:4]
while set(a) != {0}:
    cnt = 0
    while len(set(a)) != 1:
        previous = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - previous)
        cnt += 1
    print(cnt)
    a.clear()
    a = list(map(int, input().split()))[:4]
