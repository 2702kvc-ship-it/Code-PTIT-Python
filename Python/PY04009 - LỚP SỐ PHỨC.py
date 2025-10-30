def trans(x):
    if x.is_integer():
        return int(x)
    return x

for _ in range(int(input())):
    a, b, c, d = map(float, input().split())
    A = complex(a, b)
    B = complex(c, d)
    res1 = (A + B) * A
    res2 = (A + B) ** 2
    print(f"{trans(res1.real)}" + (f" + {trans(res1.imag)}i" if res1.imag > 0 else (f" - {trans(abs(res1.imag))}i" if res1.imag < 0 else "")), end=', ')
    print(f"{trans(res2.real)}" + (f" + {trans(res2.imag)}i" if res2.imag > 0 else (f" - {trans(abs(res2.imag))}i" if res2.imag < 0 else "")))