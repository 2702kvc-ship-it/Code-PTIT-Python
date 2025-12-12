ds = {}

for _ in range(int(input())):
    s = input().strip().split()
    s1 = s[0]
    s2 = ' '.join(s[1:])
    ds[s1] = s2

def hesoluong(nhom, nam):
    if nam >= 1 and nam <= 3:
        if nhom == 'A':
            return 10
        if nhom == 'B':
            return 10
        if nhom == 'C':
            return 9
        if nhom == 'D':
            return 8
    if nam >= 4 and nam <= 8:
        if nhom == 'A':
            return 12
        if nhom == 'B':
            return 11
        if nhom == 'C':
            return 10
        if nhom == 'D':
            return 9
    if nam >= 9 and nam <= 15:
        if nhom == 'A':
            return 14
        if nhom == 'B':
            return 13
        if nhom == 'C':
            return 12
        if nhom == 'D':
            return 11
    if nam >= 16:
        if nhom == 'A':
            return 20
        if nhom == 'B':
            return 16
        if nhom == 'C':
            return 14
        if nhom == 'D':
            return 13

ds2 = []
for _ in range(int(input())):
    ma = input()
    name = input()
    money = int(input())
    days = int(input())
    luong = money * days * hesoluong(ma[0], int(ma[1:3])) * 1000
    ds2.append((ma, name, ds[ma[3:]], luong))

for i in ds2:
    print(*i)