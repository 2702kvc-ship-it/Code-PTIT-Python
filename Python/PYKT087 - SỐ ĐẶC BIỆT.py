MOD = 10**9 + 7

for _ in range(int(input())):
    tmp = ''
    n, k = map(int, input().split())
    while k > 0:
        tmp += str(k % 2)
        k //= 2
    res = 0
    for i in range(len(tmp)):
        if tmp[i] == '1':
            res += (n ** i) % MOD
    print(res % MOD)