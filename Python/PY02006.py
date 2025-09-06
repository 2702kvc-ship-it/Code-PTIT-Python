def check(n, a, b):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print("YES" if check(n, a, b) else "NO")

