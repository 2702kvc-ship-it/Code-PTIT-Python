index = []

n, m = map(int, input().split())
a = [list(map(int, input().split()))[:m] for anhlandeptrai in range(n)]

def check(n):
    tmp = str(n)
    if len(tmp) > 1:
        if tmp == tmp[::-1]:
            return True
        return False
    return False

max_prime = -1

for i in range(n):
    for j in range(m):
        if check(a[i][j]):
            max_prime = max(max_prime, a[i][j])

if max_prime == -1:
    print("NOT FOUND")

else:
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_prime:
                index.append([i, j])

    print(max_prime)
    for i, j in index:
        print(f"Vi tri [{i}][{j}]")