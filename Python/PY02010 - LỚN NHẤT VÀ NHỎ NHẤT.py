s = int(input())
while s > 0:
    lon, be = -36, 1e101
    for i in range(s):
        x = input()
        x = int(x)
        lon = max(lon, x)
        be = min(be, x)
    if lon != be:
        print(be, lon)
    else:
        print("BANG NHAU")
    s = int(input())
        