def backtrack(remaining, last, cur, result):
    if remaining == 0:
        result.append(tuple(cur))
        return
    
    for i in range(last, 0, -1):
        if i <= remaining:
            cur.append(i)
            backtrack(remaining - i, i, cur, result)
            cur.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    backtrack(n, n, [], res)
    print(len(res))
    for p in res:
        print("(" + " ".join(map(str, p)) + ")", end=' ')
    print()