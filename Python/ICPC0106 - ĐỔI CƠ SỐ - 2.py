so = '0123456789ABCDEFGHIJK'

for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = int(s1, 2)
    if n == 2:
        print(s1)
    else:
        if s2 == 0:
            print(0)
            continue
        s = ""
        while s2 != 0:
            s += so[s2 % n] 
            s2 //= n
        print(s[::-1])
