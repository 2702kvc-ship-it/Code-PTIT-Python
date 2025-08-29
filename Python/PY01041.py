for _ in range(int(input())):
    s = input()
    if len(s) < 3:
        print("NO")
    else:
        smax = -1
        x = 0
        for i in range(len(s)):
            if int(s[i]) > smax:
                smax = int(s[i])
                x = i
        ok = True
        for i in range(x):
            if s[i] >= s[i + 1]:
                ok = False
                break
        for i in range(x, len(s) - 1):
            if s[i] <= s[i + 1]:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")