price = {
    ("Xe_con", 5) : "10000",
    ("Xe_con", 7) : "15000",
    ("Xe_tai", 2) : "20000",
    ("Xe_khach", 29) : "50000",
    ("Xe_khach", 45) : "70000"
}

res = {}
order = []

t = int(input())
for _ in range(t):
    bienxe, loaixe, soghe, trangthai, ngay = input().split()
    soghe = int(soghe)

    if trangthai == "IN":
        if ngay not in res:
            res[ngay] = 0
            order.append(ngay)
        res[ngay] += int(price[(loaixe, soghe)])

for ngay in order:
    print(f"{ngay}:", res[ngay])