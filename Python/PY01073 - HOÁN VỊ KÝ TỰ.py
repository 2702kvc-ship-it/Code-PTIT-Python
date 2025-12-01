def hoanvi(s):
    if len(s) == 1:
        return [s]
    res = []
    for i in range(len(s)):
        for p in hoanvi(s[:i] + s[i+1:]):
            res.append(s[i] + p)
    return res

s = input().strip()
ans = hoanvi(s)

for x in ans:
    print(x)
