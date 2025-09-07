for _ in range(int(input())):
    n = int(input())
    b = [0] * 1001
    for i in range(0, n):
        a = int(input())
        b[a] += 1

    print(b.index(max(b)))
