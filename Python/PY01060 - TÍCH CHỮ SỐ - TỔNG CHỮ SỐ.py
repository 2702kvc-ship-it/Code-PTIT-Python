for _ in range(int(input())):
    s = input()
    tich = 1
    tong = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != '0':
            tich *= int(s[i])
        else:
            tong += int(s[i])

    print(tich, tong)
    