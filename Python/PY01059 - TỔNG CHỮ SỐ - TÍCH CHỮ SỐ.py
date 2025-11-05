for _ in range(int(input())):
    n = input()
    res1, res2 = 0, 1
    check = False
    for i in range(len(n)):
        if i % 2 == 0:
            res1 += int(n[i])
        else:
            if n[i] != '0':
                res2 *= int(n[i])
                check = True
    if check:
        print(res1, res2)
    else:
        print(res1, 0)
