def check(s1, s2):
    n = len(s1)
    for i in range(n - 1):
        if abs(ord(s1[i]) - ord(s1[i + 1])) != abs(ord(s2[i]) - ord(s2[i + 1])):
            return "NO"
    return "YES"


for _ in range(int(input())):
    s1 = input()
    s2 = s1[::-1]
    print(check(s1, s2))
