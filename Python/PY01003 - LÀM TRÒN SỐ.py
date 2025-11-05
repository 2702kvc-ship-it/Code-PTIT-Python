def làm_tròn(n):
    p = 10
    while n > p:
        i = n % p
        if i >= p // 2:
            n += p
        n -= i
        p *= 10
    return n

for _ in range(int(input())):
    n = int(input())
    print(làm_tròn(n))