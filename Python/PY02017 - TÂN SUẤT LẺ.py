from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = Counter(a)
    for i in s:
        if s[i] % 2 != 0:
            print(i)
            break