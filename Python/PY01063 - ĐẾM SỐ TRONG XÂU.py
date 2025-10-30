for _ in range(int(input())):
    s1 = input()
    s2 = input()
    if len(s1) < len(s2):
        print(0)
    else:
        count = 0
        i = 0
        while i <= len(s1) - len(s2):
            if s1[i:i+len(s2)] == s2:
                count += 1
                i += len(s2)
            else:
                i += 1
        print(count)
