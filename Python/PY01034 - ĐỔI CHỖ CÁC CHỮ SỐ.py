for _ in range(int(input())):
    s = list(input().strip())
    n = len(s)
    
    i = n - 1
    while i > 0 and s[i - 1] <= s[i]:
        i -= 1
    if i == 0:
        print(-1)
        continue
    p = i - 1
    j = n - 1
    while j > p and s[j] >= s[p]:
        j -= 1
    while j - 1 > p and s[j - 1] == s[j]:
        j -= 1
    s[p], s[j] = s[j], s[p]
    if s[0] == '0':
        print(-1)
    else:
        print(''.join(s))
