n = int(input())

p = []
m = []

sum = 0
for i in range(n):
    num = int(input())
    if num > 1:
        p.append(num)
    elif num <= 0:
        m.append(num)
    else:
        sum += num

p.sort(reverse=True)
m.sort()

for i in range(0, len(p), 2):
    if i + 1 >= len(p):
        sum += p[i]
    else:
        sum += p[i] * p[i + 1]

for i in range(0, len(m), 2):
    if i + 1 >= len(m):
        sum += m[i]
    else:
        sum += m[i] * m[i + 1]

print(sum)
