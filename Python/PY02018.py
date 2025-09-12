n = int(input())
a = list(map(int, input().split()))
b = [False] * 30001
for i in a:
    b[i] = True

for i in range(1, len(b)):
    if b[i] == False:
        print(i)
        break