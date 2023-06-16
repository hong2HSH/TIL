n, m = map(int,input().split())
li = []
set = n // 6
rest = n % 6
a = 1000
b = 1000

for _ in range(m):
    x, y = map(int,input().split())
    if x < a:
        a = x
    if y < b:
        b = y
if b * 6 <= a:
    money = b * n
    li.append(money)
else:
    if b * rest > a:
        money = (set + 1) * a
        li.append(money)
    else:
        money = set * a + rest * b
        li.append(money)
print(min(li))