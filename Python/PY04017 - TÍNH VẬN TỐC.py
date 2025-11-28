start = '6:00'.split(":")

l = 120

class thisinh:
    def __init__(self, name, location, stop):
        self.name = name
        self.location = location
        s = stop.split(':')
        self.time = ((int(s[0]) - int(start[0])) * 60 + (int(s[1]) - int(start[1]))) / 60
        self.avg = round(l / self.time)
        self.id = self.code(name, location)

    def code(self, a, b):
        tmp1 = ''
        tmp2 = ''
        a, b = a.split(), b.split()
        for i in a:
            tmp1 += i[0].upper()
        for i in b:
            tmp2 += i[0].upper()
        return tmp2 + tmp1


    def __str__(self):
        return f"{self.id} {self.name} {self.location} {self.avg} Km/h"
    
ds = []    
for _ in range(int(input())):
    ds.append(thisinh(input().strip(), input().strip(), input().strip()))

ds.sort(key=lambda x: x.time)

for i in ds:
    print(i)