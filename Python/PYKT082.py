def ielts(x):
    if x > 38: return 9.0
    if x > 36: return 8.5
    if x > 34: return 8.0
    if x > 32: return 7.5
    if x > 29: return 7.0
    if x > 26: return 6.5
    if x > 22: return 6.0
    if x > 19: return 5.5
    if x > 15: return 5.0
    if x > 12: return 4.5
    if x > 9: return 4.0
    if x > 6: return 3.5
    if x > 4: return 3.0
    if x > 2: return 2.5
    return 1.0

def lamtron(avr):
    chenhlech = avr - int(avr)
    if chenhlech >= 0.75:
        return int(avr) + 1
    if chenhlech >= 0.25:
        return int(avr) + 0.5
    return float(int(avr))

t = int(input())
for _ in range(t):
    l, r, w, s = map(str, input().split())
    l, r, w, s = int(l), int(r), float(w), float(s)
    avr = (ielts(l) + ielts(r) + w + s) / 4
    print(f"{lamtron(avr):.1f}")
