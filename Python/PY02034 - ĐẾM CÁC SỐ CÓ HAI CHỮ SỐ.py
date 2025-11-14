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


from collections import Counter
count = Counter(res)

for x, y in count.items():
    print(x, y)