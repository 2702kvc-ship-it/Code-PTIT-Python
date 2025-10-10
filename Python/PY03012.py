class lophoc:
    def __init__(self, name, right, tried):
        self.name = name
        self.right = right
        self.tried = tried
    
siso = int(input())
a = []
for i in range(siso):
    name = input()
    right, tried = map(int, input().split())
    a.append(lophoc(name, right, tried))
     

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i].right < a[j].right:
            a[i], a[j] = a[j], a[i]
        elif a[i].right == a[j].right:
            if a[i].tried > a[j].tried:
                a[i], a[j] = a[j], a[i]
            elif a[i].tried == a[j].tried:
                if a[i].name > a[j].name:
                    a[i], a[j] = a[j], a[i]

for i in range(len(a)):
    print(a[i].name, a[i].right, a[i].tried)