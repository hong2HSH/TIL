s = input()
s = list(s)
s1 = list(s[0])

for i in s:
    if i != s1[-1]:
        s1.append(i)
print(len(s1) // 2)
