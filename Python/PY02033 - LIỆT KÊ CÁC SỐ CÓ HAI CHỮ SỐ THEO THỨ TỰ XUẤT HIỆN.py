s = input()
res = []
if len(s) % 2 == 0:
    for i in range(0, len(s), 2):
        tmp = '' + s[i] + s[i + 1]
        res.append(int(tmp))
else:
    for i in range(0, len(s) - 1, 2):
        tmp = '' + s[i] + s[i + 1]
        res.append(int(tmp))

final = []
for i in res:
    if i not in final:
        final.append(i)

print(*final)
