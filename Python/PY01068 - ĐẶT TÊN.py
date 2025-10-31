from itertools import combinations

ds = []

n, k = map(int, input().split())

s = input().strip().split()

for i in range(n):
    ds.append(s[i])

ds = list(set(ds))
ds.sort()

for i in combinations(ds, k):
    print(' '.join(i))
