import sys

s = sys.stdin.read().strip().split()
idx = 1

class matrix():
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def transpose(self):
        k = [[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)]
        return matrix(k)

    def mul(self, other):
        res = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    res[i][j] += self.data[i][k] * other.data[k][j]
        return matrix(res)

    def __str__(self):
        res = []
        for row in self.data:
            res.append(' '.join(map(str, row)))
        return '\n'.join(res)

for _ in range(int(s[0])):
    m, n = int(s[idx]), int(s[idx + 1])
    idx += 2
    data = [list(int(s[idx + i * n + j]) for j in range(n)) for i in range(m)]
    A = matrix(data)
    B = A.transpose()
    C = A.mul(B)
    print(C)
    idx += m * n
