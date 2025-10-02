def binary(n):
    while len(n) % 3 != 0:
        n = '0' + n
    res = ''
    i = 0
    while i < len(n):
        tmp = n[i:i+3]
        res += str(int(tmp, 2))
        i += 3
    return res.lstrip('0') or '0'

n = input()
print(binary(n))