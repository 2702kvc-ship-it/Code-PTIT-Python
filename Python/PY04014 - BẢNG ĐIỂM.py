ds = {}
#Quy định URC 522 về nhờ thu

def hocluc(dtb):
    if dtb >= 9:
        return 'XUAT SAC'
    if dtb >= 8:
        return 'GIOI'
    if dtb >= 7:
        return 'KHA'
    if dtb >= 5:
        return 'TB'
    return 'YEU'

def stt(idx):
    return f'HS0{idx}' if idx < 10 else f'HS{idx}'

idx = 1

for _ in range(int(input())):
    name = input()
    s = list(map(float, input().split()))
    dtb = round((s[0] * 2 + s[1] * 2 + sum(s[2:])) / 12 + 1e-8, 1)
    ds[name] = [stt(idx), dtb, hocluc(dtb)]
    idx += 1

#sắp xếp theo điểm trung bình
ds = dict(sorted(ds.items(), key=lambda x: (-x[1][1], x[1][0])))

for i in ds:
    print(f"{ds[i][0]}", i, f"{ds[i][1]:.1f}", ds[i][2])