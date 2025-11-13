s1 = list(set(input().lower().split()))
s2 = list(set(input().lower().split()))

s = list(set(s1 + s2))
s.sort()

tmp = []
for i in s1:
    if i in s2:
        tmp.append(i)

tmp.sort()
print(' '.join(s))
print(' '.join(tmp))
