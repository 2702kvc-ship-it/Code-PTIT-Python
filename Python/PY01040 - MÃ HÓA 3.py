def tong(s):
    total = 0
    for i in s:
        total += ord(i) - ord('A')
    r = ''
    for i in s: 
        r += chr((ord(i) - ord('A') + total) % 26 + ord('A'))
    return r

for _ in range(int(input())):
    s = input()
    a, b = tong(s[:len(s) // 2]), tong(s[len(s) // 2:])
    r = ''
    for i in range(len(a)):
        r += chr((ord(a[i]) - ord('A') + ord(b[i]) - ord('A')) % 26 + ord('A'))

    print(r)
