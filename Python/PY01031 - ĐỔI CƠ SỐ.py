import string

he = string.digits + string.ascii_uppercase

for _ in range(int(input())):
    n,coso = map(int, input().split())
    tmp = ''
    while n > 0:
        tmp = he[n % coso] + tmp
        n //= coso
    print(tmp)