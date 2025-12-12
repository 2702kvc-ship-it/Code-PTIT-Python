from decimal import Decimal, ROUND_HALF_UP

avg_list = []
ds = []
t = int(input())
for _ in range(t):
    ma = f"SV{_+1:02d}"
    name = ' '.join(input().strip().title().split())
    d1 = Decimal(input())
    d2 = Decimal(input())
    d3 = Decimal(input())
    avg = (d1 * 3 + d2 * 3 + d3 * 2) / Decimal(8)
    avg = avg.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    avg_list.append(avg)
    ds.append((ma, name, avg))

b = [1] * t
avg_list.sort(reverse=True)
for i in range(t - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if avg_list[j] > avg_list[i]:
            b[i] += 1

ds.sort(key=lambda x: -x[2])
for i in range(t):
    rank = b[i]
    print(f"{ds[i][0]} {ds[i][1]} {ds[i][2]:.2f} {rank}")



