ds = {}

team = int(input())
i = 1
for _ in range(team):
    name = input()
    school = input()
    code = f"Team{i:02d}"
    ds[code] = [name, school]
    i += 1

res = []

student = int(input())
i = 1
for _ in range(student):
    name = input()
    team_code = input()
    ma = f"C{i:03d}"
    i += 1
    if team_code in ds:
        res.append((ma, name, ds[team_code][0], ds[team_code][1]))

res.sort(key=lambda x: x[1])
for i in res:
    print(i[0], i[1], i[2], i[3])



