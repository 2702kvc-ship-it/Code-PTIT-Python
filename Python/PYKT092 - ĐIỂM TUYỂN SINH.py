uutien = {
    '1' : 1.5,
    '2' : 1.0,
    '3' : 0.0
}

ds = []

for _ in range(int(input())):
    ma = f"TS{_+1:02d}"
    name = input().strip().title()
    diem = float(input())
    dantoc = input()
    khuvuc = input()
    if dantoc != 'Kinh':
        diem += 1.5
    diem += uutien[khuvuc]
    trangthai = 'Do' if diem >= 20.5 else 'Truot'
    ds.append((ma, name, diem, trangthai))

ds.sort(key=lambda x: (-x[2], x[0]))

for i in ds:
    print(f"{i[0]} {' '.join(i[1].split())} {i[2]:.1f} {i[3]}")