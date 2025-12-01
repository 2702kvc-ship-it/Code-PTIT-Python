from itertools import permutations

def giaithua(n):
    if n == 0 or n == 1:
        return 1
    return n * giaithua(n - 1)

for _ in range(int(input())):
    s = input().strip()
    for i in range(int(s) - 1, 0, -1):
        s += str(i)
    p = giaithua(len(s))
    print(p)
    for i in permutations(s):
        print(''.join(i), end=' ')
    print()