s1 = input()
s2 = input()
vitri = int(input()) - 1
s3 = s1[:vitri] + s2 + s1[vitri:]
print(s3)