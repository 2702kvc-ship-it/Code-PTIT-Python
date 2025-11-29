maxn = 204

def solve(n, x, y, z):
    dp = [10**5] * (maxn + 1)
    dp[0] = 0
    for i in range(1, maxn + 1):
        dp[i] = min(dp[i], dp[i - 1] + x)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + z)
            dp[i] = min(dp[i], dp[i // 2 + 1] + y + z)
        else:
            dp[i] = min(dp[i], dp[(i - 1) // 2] + z + x)
            dp[i] = min(dp[i], dp[(i + 1) // 2] + y + z)

    return dp[0 : n + 10]

t = int(input())
for _ in range(t):
    n = int(input())
    x, y, z = map(int, input().split())
    print(solve(n, x, y, z))