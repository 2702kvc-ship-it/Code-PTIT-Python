def check(s):
    if len(s) != 4:
        return False
    for i in s:
        if int(i) > 255 or int(i) < 0:
            return False
    return True

t = int(input())
for x in range(t):
    try:
        s = input().split('.')
        print('YES' if check(s) else 'NO')
    except:
        print('NO')
