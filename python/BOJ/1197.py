v, e = map(int, input().split())
li = set()
for _ in range(e):
    a, b, c = map(int, input().split())
    li.add(c)
print(min(li))
