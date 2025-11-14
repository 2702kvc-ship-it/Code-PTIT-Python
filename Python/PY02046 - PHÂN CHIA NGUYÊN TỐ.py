def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))[:n]
b = []
for i in a:
    if i not in b:
        b.append(i)
flag = False
for i in range(len(b)):
    s1 = sum(b[:i + 1])
    s2 = sum(b[i + 1:]) if i + 1 < len(b) else 0
    if prime(s1) and prime(s2):
        print(i)
        flag = True
        break

if not flag:
    print('NOT FOUND')