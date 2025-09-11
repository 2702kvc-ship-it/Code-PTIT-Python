for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(m, len(a)):
        print(a[i], end=" ")
    for i in range(m):
        print(a[i], end=" ")
    print()
    
