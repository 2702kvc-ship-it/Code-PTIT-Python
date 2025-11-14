n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

# a & b
c = list(sorted(a & b))
# a - b
d = list(sorted(a - b))
# b - a
e = list(sorted(b - a))

print(*c)
print(*d)
print(*e)