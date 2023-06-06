T = int(input())

for _ in range(T):
    a = int(input())
    li = [a]
    while 1:
        for i in li:
            if i > 1:
                li.remove(i)
                li.append(i - 1)
                li.append(i - 2)
            else:
                continue
    print(li)
