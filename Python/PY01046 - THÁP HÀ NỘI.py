def move(a, b, c, n):
    if n == 0:
        return
    move(a, c, b, n - 1)
    print(f"{a} -> {c}")
    move(b, a, c, n - 1)
    
n = int(input())
move('A', 'B', 'C', n)