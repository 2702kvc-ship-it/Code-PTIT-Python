import string

hehe = string.ascii_uppercase

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = 'A'
    for i in range(1, n):
        s = s + hehe[i] + s
    
    print(s[k - 1])

