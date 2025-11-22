import sys

n, m = map(int, input().split())
a = [list(map(str, input().split())) for _ in range(n)]

def check(x):
    if len(x) < 2:
        return False
    if x == x[::-1]:
        return True
    return False

max_value = -1

flag = False

for i in range(n):
    for j in range(m):
        if check(a[i][j]):
            max_value = max(max_value, int(a[i][j]))
            flag = True

if not flag:
    print("NOT FOUND")
    sys.exit()

else:
    print(max_value)

for i in range(n):
    for j in range(m):
        if int(a[i][j]) == max_value:
            print(f"Vi tri [{i}][{j}]")