def cung_hoang_dao(d, m):
    if (m == 3 and d >= 21) or (m == 4 and d <= 19):
        return 'Bach Duong'
    if (m == 4 and d >= 20) or (m == 5 and d <= 20):
        return 'Kim Nguu'
    if (m == 5 and d >= 21) or (m == 6 and d <= 20):
        return 'Song Tu'
    if (m == 6 and d >= 21) or (m == 7 and d <= 22):
        return 'Cu Giai'
    if (m == 7 and d >= 23) or (m == 8 and d <= 22):
        return 'Su Tu'
    if (m == 8 and d >= 23) or (m == 9 and d <= 22):
        return 'Xu Nu'
    if (m == 9 and d >= 23) or (m == 10 and d <= 22):
        return 'Thien Binh'
    if (m == 10 and d >= 23) or (m == 11 and d <= 22):
        return 'Thien Yet'
    if (m == 11 and d >= 23) or (m == 12 and d <= 21):
        return 'Nhan Ma'
    if (m == 12 and d >= 22) or (m == 1 and d <= 19):
        return 'Ma Ket'
    if (m == 1 and d >= 20) or (m == 2 and d <= 18):
        return 'Bao Binh'
    if (m == 2 and d >= 19) or (m == 3 and d <= 20):
        return 'Song Ngu'

for _ in range(int(input())):
    d, m = map(int, input().split())
    print(cung_hoang_dao(d, m))
