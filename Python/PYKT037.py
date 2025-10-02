coso = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#anh Lân đẹp trai
#anh Lân siêu cấp vũ trụ
#anh Lân ngầu lòi
#anh Lân dễ thương

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 0:
        print(0)
        continue
    res = ''
    while a > 0:
        res = coso[a % b] + res
        a //= b
    print(res)