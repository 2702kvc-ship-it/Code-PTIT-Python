from datetime import datetime

price = {
    '1' : 25,
    '2' : 34,
    '3' : 50,
    '4' : 80
}

class bill:
    def __init__(self, name, room, check_in, check_out, extra):
        self.code = "KH{:02d}".format(len(ds) + 1)
        self.name = name
        self.room = room
        self.date = (datetime.strptime(check_out, "%d/%m/%Y") - 
                    datetime.strptime(check_in, "%d/%m/%Y")).days + 1
        self.extra = extra
        self.total = self.date * price[self.room[0]] + self.extra

    def __str__(self):
        return f"{self.code} {self.name} {self.room} {self.date} {self.total}"


ds = []


for _ in range(int(input())):
    ds.append(bill(input(), input(), input().strip(), input().strip(), int(input())))

ds.sort(key=lambda x: -x.total)

for i in ds:
    print(i)