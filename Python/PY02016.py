from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = Counter(a)
    so, tansuat = x.most_common(1)[0]
    if tansuat > n // 2:
        print(so)
    else:
        print("NO")