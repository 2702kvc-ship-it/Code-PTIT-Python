n = int(input())
a = list(map(int, input().split()))

k = 1e9 + 7
value = -36

for i in range(n):
    step = 0
    for j in range(n):
        if i != j:
            step += abs(a[i] - a[j])
    if step < k:
        k = step
        value = a[i]

print(k, value)
