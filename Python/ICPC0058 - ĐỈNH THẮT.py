import sys
sys.setrecursionlimit(10000)

def dfs(u, v, blocked, adj, check):
    if u == v:
        return True
    check[u] = True
    for x in adj[u]:
        if not check[x] and x != blocked:
            if dfs(x, v, blocked, adj, check):
                return True
    return False

for _  in range(int(input())):
    n, m, u, v = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)

    res = 0
    for i in range(1, n + 1):
        if i == u or i == v:
            continue
        check = [False] * (n + 1)
        if not dfs(u, v, i, adj, check):
            res += 1

    print(res)


    
