n = input().split("-")
li = []

for i in n:
    a = list(map(int, i.split("+")))
    if len(a) == 1:
        li.append(int(a[0]))
        continue
    else:
        b = sum(a)
        li.append(b)
sum = li[0]
for j in range(1, len(li)):
    sum -= li[j]
print(sum)
