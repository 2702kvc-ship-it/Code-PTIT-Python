sj = {
    'A' : "TOAN",
    'B' : "LY",
    'C' : "HOA"
}

ut = {
    '1' : 2.0,
    '2' : 1.5,
    '3' : 1.0,
    '4' : 0.0
}

class Gv:
    def __init__(self, name, ma, d1, d2):
        self.name = name
        self.id = 'GV{:02d}'.format(len(ds) + 1)
        self.monhoc = sj[ma[0]]
        self.diem = float(d1) * 2 + float(d2) + ut[ma[1]]
        self.trangthai = 'TRUNG TUYEN' if self.diem >= 18 else 'LOAI'

    def __str__(self):
        return f"{self.id} {self.name} {self.monhoc} {self.diem:.1f} {self.trangthai}"
    
ds = []

for _ in range(int(input())):
    name = input().strip()
    ma = input().strip()
    d1 = float(input())
    d2 = float(input())
    ds.append(Gv(name, ma, d1, d2))

ds.sort(key=lambda x: -x.diem)

for i in ds:
    print(i)