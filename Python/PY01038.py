for _ in range(int(input())):
    n = int(input())
    ok = False
    for i in range(0, 1000):
        if n % 7 == 0:
            ok = True
            print(n)
            break
        else:
            tmp = str(n)
            n += int(tmp[::-1])
    if ok == False:
        print(-1)