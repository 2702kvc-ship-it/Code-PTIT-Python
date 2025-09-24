import sys
input = sys.stdin.readline

def change(n, p, q):
    tmp = ""  #python không cho sửa trực tiếp trong chuỗi:)
    for i in range(len(n)):
        if n[i] == p:
            tmp += q
        else:
            tmp += n[i]
    return tmp

data = sys.stdin.read().split() #phải đọc hết dữ liệu trong chuỗi vì có thể thằng so1 so2 cùng nằm trên 1 dòng
t = data[0]
idx = 1
for _ in range(int(t)):
    p, q = data[idx + 0], data[idx + 1]
    so1, so2 = data[idx + 2], data[idx + 3]
    plon = str(max(int(p), int(q)))
    qbe = str(min(int(p), int(q)))
    rmax = int(change(so1, qbe, plon)) + int(change(so2, qbe, plon))
    rmin = int(change(so1, plon, qbe)) + int(change(so2, plon, qbe))
    print(rmin, rmax) #ctrl Z để chạy
    idx += 4

    
    

