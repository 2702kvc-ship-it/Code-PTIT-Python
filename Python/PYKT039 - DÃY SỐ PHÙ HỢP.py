t = int(input())

def check(a, b, n):
    for i in range(n):
        if a[i] > b[i]:
            return "NO"
    return "YES"

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    a.sort()
    b.sort()
    print(check(a, b, n))