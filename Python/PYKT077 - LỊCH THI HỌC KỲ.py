m, n = map(int, input().split())
ds1 = {}
for _ in range(m):
    ma = input()
    name = input()
    ds1[ma] = name

ds2 = []
for _ in range(n):
    s = input().split()
    mathi = s[0]
    ngay = s[1]
    gio = s[2]
    nhom = s[3]
    macathi = f"T{_+1:03d}"
    ds2.append((macathi, mathi, ds1[mathi], ngay, gio, nhom))

ds2.sort(key=lambda x: (x[3][6:] + x[3][3:5] + x[3][0:2], x[4][:2] + x[4][3:], x[0]))

for i in ds2:
    print(*i)