n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)

def check(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

flag = False

for i in range(len(b)):
    sum1 = sum(b[:i + 1])
    sum2 = sum(b[i + 1:]) if i + 1 < len(b) else 0
    if check(sum1) and check(sum2):
        print(i)
        flag = True
        break

if not flag:
    print("NOT FOUND")