for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(set(a))
    bmin = min(b)
    bmax = max(b)
    print((bmax - bmin + 1) - len(b))