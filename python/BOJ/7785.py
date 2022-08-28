n = int(input())
li = []

for i in range(n):
    a, b = map(str,input().split())
    if b == 'enter':
        li.append(a)
    elif b == 'leave':
        li.remove(a)
li.sort(reverse=True)
print(*li, sep='\n')