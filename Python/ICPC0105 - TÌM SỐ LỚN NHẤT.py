for _ in range(int(input())):
    s = input()
    tmp = ""
    smax = -20
    for i in s:
        if '0' <= i <= '9':
            tmp += i
        else:
            if tmp != "":
                smax = max(smax, int(tmp))
                tmp = ""
    if tmp != "":
        smax = max(smax, int(tmp))
    print(smax if smax != -20 else -1)