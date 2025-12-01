ds = []
for _ in range(int(input())):
    ma = input().strip()
    mon = input().strip()
    hinhthuc = input().strip()
    ds.append((ma, mon, hinhthuc))

ds.sort(key=lambda x: x[0])

for i in ds:
    print(*i)