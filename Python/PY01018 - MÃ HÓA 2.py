p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
def inx(x):
    return (p.index(x))
while True:
    s = input()
    if s[0] == '0': 
        break
    k, s = s.split()
    ans = [p[(inx(x) + int(k)) % 28] for x in s]
    print(''.join(reversed(ans)))