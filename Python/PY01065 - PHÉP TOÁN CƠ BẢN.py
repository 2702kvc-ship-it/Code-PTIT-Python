def result(a, op, b, c):
    if op == '+':
        return a + b == c
    if op == '-':
        return a - b == c
    if op == '*':
        return a * b == c
    if a % b == 0:
        return a // b == c
    return False

def step1(a):
    ans = []
    if a[0] == '?':
        for i in range(1, 10):
            ans.append(str(i) + a[1:])
    else:
        ans.append(a)
    r = []
    if a[1] == '?':
        for i in ans:
            for j in range(0, 10):
                r.append(i[0] + str(j))
    else:
        r = ans
    return r

def step2(a):
    if a == '?':
        return '+-*/'
    return [a]

def solve(s):
    arr = s.split()
    a = step1(arr[0])
    op = step2(arr[1])
    b = step1(arr[2])
    c = step1(arr[4])
    for i in a:
        for j in op:
            for k in b:
                for l in c:
                    if result(int(i), j, int(k), int(l)):
                        return f"{i} {j} {k} = {l}"
    return 'WRONG PROBLEM!'


for _ in range(int(input())):
    print(solve(input()))