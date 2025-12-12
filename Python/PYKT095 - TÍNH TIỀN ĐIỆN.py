dinhmuc = {
    'A' : 100,
    'B' : 500,
    'C' : 200
}

ds = []

for _ in range(int(input())):
    makh = f'KH{_ + 1:02d}'
    name = ' '.join(input().strip().title().split())
    s = input().split()
    ma = s[0]
    t1, t2 = int(s[1]), int(s[2])
    hieu = t2 - t1
    tien1 = 0
    tien2 = 0
    if hieu <= dinhmuc[ma]:
        tien1 = hieu * 450
    else:
        tien1 = dinhmuc[ma] * 450
        tien2 = (hieu - dinhmuc[ma]) * 1000
    vat = tien2 // 20 # 5%
    tong = tien1 + tien2 + vat
    ds.append((makh, name, tien1, tien2, vat, tong))

ds.sort(key=lambda x: -x[5])

for i in ds:
    print(*i)


