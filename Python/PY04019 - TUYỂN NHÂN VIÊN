def danhgia(n):
    if n < 5:
        return 'TRUOT'
    if n < 8:
        return 'CAN NHAC'
    if n <= 9.5:
        return 'DAT'
    return 'XUAT SAC'

ds = []

def stt(idx):
    return 'TS0' + str(idx) # Khắm chó vl éo giống mọi bài khác :v

for idx in range(1, int(input()) + 1):
    name = input()
    dlt = input()
    dlt = float(dlt)
    if dlt > 10:
        dlt /= 10
    dth = input()
    dth = float(dth)
    if dth > 10:
        dth /= 10
    dtc = (dlt + dth) / 2
    ds.append([stt(idx), name, dtc, danhgia(dtc)])

ds = list(sorted(ds, key=lambda x: -x[2]))

for i in range(len(ds)):
    print(ds[i][0], ds[i][1], f"{ds[i][2]:.2f}", ds[i][3])
