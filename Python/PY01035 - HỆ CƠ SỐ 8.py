#chuyển từ hệ 10 sang hệ 8

n = input()
while len(n) % 3 != 0:
    n = '0' + n
tmp = ''
i = 0
while i + 3 <= len(n):
    k = n[i : i + 3]
    tmp += str(int(k, 2))
    i += 3

print(tmp)