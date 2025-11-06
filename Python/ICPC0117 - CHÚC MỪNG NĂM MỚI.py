a = []
for _ in range(int(input())):
    s = input()
    if s not in a:
        a.append(s)

print(len(a))