n, k = map(int, input().split())
li = []

for _ in range(n):
    w, v = map(int, input().split())
    li.append([w, v])

li.sort(key=lambda x: x[1], reverse=True)

x = k
y = 0
print(li)

for i in li:
    if i[0] > k:
        continue
    if i[0] <= x:
        y += i[1]
        x -= i[0]
    else:
        if i[1] > y:
            y = i[1]
            x = k - i[0]
        else:
            continue
print(y)
