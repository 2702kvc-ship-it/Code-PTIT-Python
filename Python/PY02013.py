a = int(input())
while a != 0:
    cnt = 1
    while a != 1:
        if a % 2 == 0:
            a //= 2
        else:
            a = a * 3 + 1
        cnt += 1
    print(cnt)
    a = int(input())