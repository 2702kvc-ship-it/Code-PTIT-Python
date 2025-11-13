from collections import Counter

he3 = '012'

def check(s):
    c = Counter(s)
    if c['2'] > len(s) // 2:
        return True
    return False

def convert(z):
    s = ''
    while z > 0:
        s = he3[z % 3] + s
        z //= 3
    return s

for _ in range(int(input())):
    n = int(input())
    res = []
    cnt = 0
    z = 1
    s = ''
    while cnt < n:
        s = convert(z)
        if check(s):
            res.append(s)
            cnt += 1
        z += 1
    print(' '.join(res))
    
