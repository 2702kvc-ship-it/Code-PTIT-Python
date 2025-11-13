def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime

s = sieve(10 ** 6)

n = int(input())
a = list(map(int, input().split()))

step = 0

for i in range(n):
    if s[a[i]]:
        continue
    else:
        l, r = 0, 0
        k = a[i]
        while s[k] == False:
            l += 1
            k -= 1
        k = a[i]
        while s[k] == False:
            r += 1
            k += 1
        step = max(step, min(l, r))

print(step)

#cảm giác bài này chưa đúng lắm vì mình chưa kiểm tra 2 cận của list a mà vẫn AC