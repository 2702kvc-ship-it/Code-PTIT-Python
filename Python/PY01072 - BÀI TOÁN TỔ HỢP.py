from itertools import combinations as lgs

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = set(a)
a = sorted(list(a))

for i in lgs(a, k):
    print(*i)