N = int(input())
li = []
for _ in range(N):
    li.append(input())
li = set(li)
li = list(li)
li.sort()
li.sort(key=len)

for i in li:
    print(i)
