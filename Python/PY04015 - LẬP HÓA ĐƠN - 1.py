def phuphi(n):
    if n <= 50:
        return 1.02
    if n <= 100:
        return 1.03
    return 1.05

def money(n):
    if n <= 50:
        return n * phuphi(n) * 100
    if n <= 100:
        return 50 * phuphi(n) * 100 + (n - 50) * phuphi(n) * 150
    if n > 100:
        return 50 * phuphi(n) * 100 + 50 * phuphi(n) * 150 + (n - 100) * phuphi(n) * 200

def stt(n):
    if n < 10:
        return 'KH0' + str(n)
    return 'KH' + str(n)

idx = 1
ds = {}

for _ in range(int(input())):
    name = input()
    s1 = int(input())
    s2 = int(input())
    tong = s2 - s1
    ds[name] = [stt(idx), money(tong)]
    idx += 1

ds = dict(sorted(ds.items(), key=lambda x: -x[1][1]))

for i in ds:
    print(f"{ds[i][0]} {i} {ds[i][1]:.0f}")
