for _ in range(int(input())):
    s = input().strip()
    if len(s) <= 100:
        print(s)
    else:
        for i in range(98, -1, -1):
            if s[i] == ' ':
                print(s[:i])
                break