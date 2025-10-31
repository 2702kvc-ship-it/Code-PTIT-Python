ds = {}
#Quy định URC 522 về nhờ thu

for _ in range(int(input())):
    tram = input()
    timestart = input().split(':')
    timestop = input().split(':')
    time = (int(timestop[0]) * 60 + int(timestop[1]) - int(timestart[0]) * 60 - int(timestart[1]))
    value = int(input())
    if tram not in ds:
        ds[tram] = [0, 0]
        ds[tram][0] += time
        ds[tram][1] += value

    else:
        ds[tram][0] += time
        ds[tram][1] += value

idx = 1
for i in ds:
    print(f"T0{idx}" if idx < 10 else f"T{idx}", end=' ')
    print(i, f'{ds[i][1] / (ds[i][0] / 60):.2f}')
    idx += 1
