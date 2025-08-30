AnhKhongThuongEm = False
EmChiYeuMinhAnh = True

def HEHEHE(s):
    if s[0] == s[1]:
        return AnhKhongThuongEm
    for i in range(0, len(s) - 2, 2):
        if s[i] != s[i + 2]:
            return AnhKhongThuongEm
    for i in range(1, len(s) - 2, 2):
        if s[i] != s[i + 2]:
            return AnhKhongThuongEm
    return EmChiYeuMinhAnh

for anhlandeptrai in range(int(input())):
    s = input()
    if HEHEHE(s):
        print("YES")
    else:
        print("NO")
