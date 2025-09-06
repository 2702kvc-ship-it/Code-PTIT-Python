a = []
while len(a) < 10:
    a.extend(map(int, input().split()))

b = set(x % 42 for x in a)
print(len(b))


