ds = {}

n, m = map(int, input().split())
i = 1
for _ in range(n):
    theloai = input()
    matheloai = f"TL{i:03d}"
    ds[matheloai] = theloai
    i += 1
res = []
i = 1
for _ in range(m):
    ma = input()
    ngaychieu = input()
    name = input()
    sotap = int(input())
    maphim = f"P{i:03d}"
    i += 1
    if ma in ds:
        res.append((maphim, ds[ma], ngaychieu, name, sotap))

res.sort(key=lambda x: (x[2][6:] + x[2][3:5] + x[2][:2], x[3], -x[4]))

for i in res:
    print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]}")