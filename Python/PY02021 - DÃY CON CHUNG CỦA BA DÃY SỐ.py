for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a1 = list(map(int, input().split()))[:n]
    a2 = list(map(int, input().split()))[:m]
    a3 = list(map(int, input().split()))[:k]

    i, j = 0, 0
    tmp, res = [], []
    while i < n and j < m:
        if a1[i] == a2[j]:
            tmp.append(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1

    i, j = 0, 0
    while i < len(tmp) and j < k:
        if tmp[i] == a3[j]:
            res.append(tmp[i])
            i += 1
            j += 1
        elif tmp[i] < a3[j]:
            i += 1
        else:
            j += 1

    if len(res) == 0:
        print("NO")
    else:
        print(*res)