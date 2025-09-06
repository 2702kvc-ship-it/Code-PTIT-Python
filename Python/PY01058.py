from math import *

def snt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        s4 = s[-4:]
        print("YES" if snt(int(s4)) else "NO")