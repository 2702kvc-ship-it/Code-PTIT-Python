def chuso(s):
    tong = 0
    for i in s:
        tong += int(i)
    if tong % 10 == 0:
        return True
    return False

for _ in range(int(input())):
    s = input()
    if chuso(s):
        ok = True
        for i in range(0, len(s) - 1):
            if abs(int(s[i]) - int(s[i+1])) != 2:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")