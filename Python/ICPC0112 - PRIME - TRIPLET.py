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

if __name__ == '__main__':
    p = sieve(10 ** 6)
    t = int(input())
    for _ in range(t):
        n = int(input())
        i = 0
        dem = 0
        while p[i + 2] <= n:
            if (p[i + 1] - p[i] == 2 or p[i + 1] - p[i] == 4) and p[i + 2] - p[i] == 6: 
                dem += 1
            i += 1
        print(dem)