class ThiSinh():
    def __init__(self, ten, birth, diem1, diem2, diem3):
        self.ten = ten
        self.birth = birth
        self.sum = diem1 + diem2 + diem3

    def __str__(self):
        return f"{self.ten} {self.birth} {self.sum:.1f}"
    

s = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
print(s)