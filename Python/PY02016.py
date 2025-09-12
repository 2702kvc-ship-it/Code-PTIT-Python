t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (10 ** 6 + 1)
    for i in a:
        b[i] += 1
    if max(b) > n // 2:
        print(b.index(max(b)))
    else:
        print("NO")
