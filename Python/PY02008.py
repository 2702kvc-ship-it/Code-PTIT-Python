def sieve(n):
    a = [True] * (n + 1)
    a[0] = a[1] = False
    p = 2
    while p * p <= n:
        if a[p]:
            for i in range(p * p, n + 1, p):
                a[i] = False
        p += 1
    b = [i for i in range(2, n + 1) if a[i]]
    return b

kc = sieve(999999)
a, b = map(int, input().split())
print(b, end=" ")
for i in range(a):
    b += kc[i]
    print(b, end=" ")