n = input()
def step(n):
    if len(n) == 1:
        return 0
    sum = 0
    for i in n:
        sum += ord(i) - ord('0')
    return step(str(sum)) + 1

if len(n) <= 1:
    print(1)
else:
    print(step(n))