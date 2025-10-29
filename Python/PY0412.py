class sinhvien():
    def __init__(self, masv, ten, malop):
        self.ten = ten
        self.masv = masv
        self.malop = malop
        self.diem = 10
    def tinhdiemcc(self, diemdanh):
        vang = diemdanh.count('v')
        muon = diemdanh.count('m')
        self.diem = max(0, self.diem - 2 * vang - muon)
    def __str__(self):
        if self.diem == 0:
            return f"{self.masv} {self.ten} {self.malop} {self.diem} KDDK"
        return f"{self.masv} {self.ten} {self.malop} {self.diem}"
    

t = int(input())
ds = {}
for i in range(t):
    sv = sinhvien(input(), input(), input())
    ds[sv.masv] = sv
for i in range(t):
    masv, diemdanh = input().split()
    ds[masv].tinhdiemcc(diemdanh)
for i in ds:
    print(ds[i])

print(ds)
