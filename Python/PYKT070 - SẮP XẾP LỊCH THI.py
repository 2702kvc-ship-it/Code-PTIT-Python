from datetime import datetime

# ---- ĐỌC FILE MONTHI ----
f = open("MONTHI.in")
t = int(f.readline().strip())

mon = {}
for _ in range(t):
    mamon = f.readline().strip()
    tenmon = f.readline().strip()
    hinhthuc = f.readline().strip()
    mon[mamon] = tenmon
f.close()


# ---- ĐỌC FILE CATHI ----
f = open("CATHI.in")
t = int(f.readline().strip())

ca = {}
for i in range(1, t + 1):
    ngay = f.readline().strip()
    gio = f.readline().strip()
    phong = f.readline().strip()
    maca = f"C{i:03d}"
    ca[maca] = (ngay, gio, phong)
f.close()


# ---- ĐỌC FILE LICHTHI ----
f = open("LICHTHI.in")
t = int(f.readline().strip())

ds = []
for _ in range(t):
    maca, mamon, nhom, sv = f.readline().strip().split()
    ngay, gio, phong = ca[maca]
    tenmon = mon[mamon]
    dt = datetime.strptime(ngay + " " + gio, "%d/%m/%Y %H:%M")
    ds.append((dt, maca, ngay, gio, phong, tenmon, nhom, sv))
f.close()

# ---- SORT ----
ds.sort(key=lambda x: (x[0], x[1]))

# ---- OUTPUT ----
for item in ds:
    _, _, ngay, gio, phong, tenmon, nhom, sv = item
    print(ngay, gio, phong, tenmon, nhom, sv)