def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if prime(i):
        b.append(i)

b.sort()
idx = 0
for i in range(len(a)):
    if prime(a[i]):
        print(b[idx], end=' ')
        idx += 1
    else:
        print(a[i], end=' ')