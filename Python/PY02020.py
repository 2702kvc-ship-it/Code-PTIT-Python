n = int(input())
a = list(map(float, input().split()))[:n]
amax = max(a)
amin = min(a)
while True:
    if amax in a:
        a.remove(amax)
    elif amin in a:
        a.remove(amin)
    else:
        break

tbc = sum(i for i in a) / len(a)
print(f"{tbc:.2f}")
