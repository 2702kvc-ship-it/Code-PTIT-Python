for _ in range(int(input())):
    n = int(input())
    a = [sorted(list(map(int, input().split()))) for _ in range(n)]
    a.sort(key=lambda x: x[1])
    cnt = 0
    end = -1
    for s, e in a:
        if s >= end:
            cnt += 1
            end = e

    print(cnt)