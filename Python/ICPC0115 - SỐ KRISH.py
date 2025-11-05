def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)

for _ in range(int(input())):
    n = int(input())
    n = str(n)
    res = 0
    for i in n:
        res += giaithua(int(i))
    if res == int(n):
        print("Yes")
    else:
        print("No")