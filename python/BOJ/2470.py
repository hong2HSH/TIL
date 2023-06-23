n = int(input())
plus = []
minus = []

for i in n:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)
print(plus, minus)
