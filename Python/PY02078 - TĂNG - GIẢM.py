for _ in range(int(input())):
    n = int(input())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for i in range(n):
        a[i], b[i] = map(float, input().split())

    dp = [1] * (n + 1)
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and b[j] > b[i]:
                dp[i] = max(dp[i], dp[j] + 1) 
    
    print(max(dp)) 
