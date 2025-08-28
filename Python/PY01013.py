import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


for _ in range(int(input())):
    a, b = map(int, input().split())
    c = str(math.gcd(a, b))
    tong = 0
    for i in c:
        tong += int(i)
    if prime(tong):
        print("YES")
    else:
        print("NO")