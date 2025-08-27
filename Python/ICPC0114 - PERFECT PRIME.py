from math import *

def snt(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n > 1

for _ in range(int(input())):
    s1 = input()
    s2 = s1[::-1]
    if snt(int(s1)) and snt(int(s2)):
        tong = 0
        for i in s1:
            tong += int(i)
        if snt(tong):
            ok = 1
            for i in s1:
                if not snt(int(i)):
                    ok = 0
                    break
            if ok == 1:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")