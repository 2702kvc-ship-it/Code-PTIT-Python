t = int(input())
for _ in range(t):
    s = input().strip()
    tmp = ''
    s2 = 0
    for i in s:
        if i.isalpha():
            tmp += i
        elif i.isdigit():
            s2 += ord(i) - ord('0')
    s1 = ''.join(sorted(tmp))
    print(s1 + str(s2))