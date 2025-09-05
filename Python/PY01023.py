from math import *

def thuasonguyento(n):
    if n == 1:
        print(1)
    else:
        print("1 *", end=" ")
        for i in range(2, int(sqrt(n)) + 1):
            dem = 0
            ok = False
            while n % i == 0:  
                ok = True
                dem += 1
                n //= i
            if ok == True:
                print(f"{i}^{dem}",end = " ")
            if n != 1 and ok == True:
                print("*", end=" ")
        if n != 1:
            print(f"{n}^1")
        else:
            print()

for _ in range(int(input())):
    n = int(input())
    thuasonguyento(n)
