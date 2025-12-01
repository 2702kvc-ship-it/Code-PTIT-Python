def thuannghich(n):
    return n == n[::-1]

maxlen = 0

with open("VANBAN.in", "r") as f:
    data = f.read().split()
    for word in data:
        if thuannghich(word):
            if len(word) > maxlen:
                maxlen = len(word)
    ds = {}
    for word in data:
        if thuannghich(word) and len(word) == maxlen:
            if word not in ds:
                ds[word] = 1
            else:
                ds[word] += 1

    for w, f in ds.items():
        print(w, f)
            
    