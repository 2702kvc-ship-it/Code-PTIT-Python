def check(n):
    if len(n) % 2 == 0:
        return False
    if n[0] == n[1]:
        return False
    for i in range(0, len(n) - 1, 2):
        if n[i] != n[i + 2]:
            return False
    return True

for _ in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")