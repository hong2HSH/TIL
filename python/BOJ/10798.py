li = []
le = []
for ii in range(5):
    a = list(input())
    li.append(a)
    le.append(len(a))
m = max(le)
for i in range(m):
    for j in range(5):
        if i >= len(li[j]):
            continue
        else:
            print(li[j][i], end='')