from collections import Counter

for _ in range(int(input())):
    s1 = input()
    s2 = input()
    print(f"Test {_ + 1}: " + ("YES" if Counter(s1) == Counter(s2) else "NO"))