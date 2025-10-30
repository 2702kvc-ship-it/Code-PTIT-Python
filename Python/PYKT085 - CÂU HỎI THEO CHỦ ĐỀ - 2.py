t = int(input())
ds = {}
check = None
for i in range(t):
    s = input().strip()
    if s == "":
        check = None
        continue
    if check is None:
        check = s
        ds[check] = 0
    else:
        ds[check] += 1

for key, value in ds.items():
    print(f"{key}: {value}")