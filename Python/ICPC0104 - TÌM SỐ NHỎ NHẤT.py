for _ in range(int(input())):
    s = input()
    tmp = ""
    smin = 1e19
    for i in s:
        if ord('0') <= ord(i) <= ord('9'):
            tmp += i
        else:
            if tmp != "":
                smin = min(smin, int(tmp))
                tmp = ""
    if tmp != "":
        smin = min(smin, int(tmp))
    print(smin if smin != 1e19 else -1)
