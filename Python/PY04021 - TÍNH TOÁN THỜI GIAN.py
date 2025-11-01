class Player:
    def __init__(self, ma, ten, come, out):
        self.ma = ma
        self.ten = ten
        come = come.split(':')
        out = out.split(':')
        self.tong = int(out[0]) * 60 + int(out[1]) - int(come[0]) * 60 - int(come[1])
    def __str__(self):
        gio = self.tong // 60
        phut = self.tong % 60
        return f"{self.ma} {self.ten} {gio} gio {phut} phut"

ds = []

gamer = int(input())
for _ in range(gamer):
    x = Player(input().strip(), input().strip(), input().strip(), input().strip())
    ds.append(x)

ds = list(sorted(ds, key=lambda x: -x.tong))
for i in ds:
    print(i)