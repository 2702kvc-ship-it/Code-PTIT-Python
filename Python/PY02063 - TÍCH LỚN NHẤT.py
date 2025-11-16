n = int(input())
a = list(map(int, input().split()))[:n]
a.sort()
t1 = a[-1] * a[-2]
t2 = a[0] * a[1]
t3 = a[-1] * a[-2] * a[-3]
t4 = a[0] * a[1] * a[2]
t5 = a[0] * a[1] * a[-1]

print(max(t1, t2, t3, t4, t5))
