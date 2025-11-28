ds = []

class sp:
    def __init__(self, ma, ten, sl, dg, ck):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.dg = dg
        self.ck = ck
        self.total = self.sl * self.dg - self.ck

    def __str__(self):
        return f"{self.ma} {self.ten} {self.sl} {self.dg} {self.ck} {self.total}"
    

for _ in range(int(input())):
    ds.append(sp(input().strip(), input().strip(), int(input()), int(input()), int(input())))

ds.sort(key=lambda x: -x.total)

for i in ds:
    print(i)