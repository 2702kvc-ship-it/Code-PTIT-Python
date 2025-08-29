import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    n = input()
    s1 = ""
    s2 = ""
    if len(n) < 4:
        print("NO")
    else:
        s1 = n[0] + n[1] + n[2]
        s2 = n[len(n) - 3] + n[len(n) - 2] + n[len(n) - 1]
        if prime(int(s1)) and prime(int(s2)):
            print("YES")
        else:
            print("NO")