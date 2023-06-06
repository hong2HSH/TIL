max = 0
li = []

for i in range(9):
    a = int(input())
    li.append(a)
    if a > max:
        max = a
    else:
        continue
print(max)
print(li.index(max) + 1)
