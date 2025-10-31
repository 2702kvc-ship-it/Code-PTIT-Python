t = int(input())

a = []

while len(a) < t:
    a += list(map(int, input().split()))

b = []
for i in a:
    if i % 2 == 0:
        b.append('Chan')
    else:
        b.append('Le')

l1 = []
l2 = []
for i in a:
    if i % 2 == 0:
        l1.append(i)
    else:
        l2.append(i)

l1.sort()
l2.sort(reverse=True)        

idx1, idx2 = 0, 0
res = []
for i in b:
    if i == 'Chan':
        res.append(l1[idx1])
        idx1 += 1
    else:
        res.append(l2[idx2])
        idx2 += 1

print(*res)