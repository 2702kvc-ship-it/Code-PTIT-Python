def check(n):
    streak = 0
    if n[0] == '8':
        return 'NO'
    for i in n:
        if i != '6' and i != '8':
            return 'NO'
        if i == '8':
            streak += 1
        else:
            streak = 0
        if streak == 3:
            return 'NO'
    return 'YES'

n = input()
print(check(n))