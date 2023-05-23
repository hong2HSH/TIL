N = int(input())
book = dict()

for _ in range(N):
    a = input()
    if a in book:
        book[a] += 1
    else:
        book[a] = 1
num = max(book.values())
list = []
for ans in book:
    if num == book[ans]:
        list.append(i)
list.sort()
print(list[0])
