for _ in range(int(input())):
    s = input()
    if s.count('(') != s.count(')'):
        print(-1)
        continue
    check = []
    for i in s:
        if i == '(' or i == ')':
            check.append(i)
    a = [0] * len(check)
    value = 1
    for i in range(0, len(check)):
        if check[i] == '(':
            a[i] = value
            value += 1
    maxa = max(a)
    while 0 in a:
        for i in range(0, len(a) - 1):
            if a[i] == maxa:
                for j in range(i + 1, len(a)):
                    if a[j] == 0:
                        a[j] = maxa
                        maxa -= 1
                        break
    print(*a)