from collections import Counter

T = int(input())

for _ in range(T):
    a = int(input())
    li = [a]
    for _ in range(a):
        for i in li:
            if i > 1:
                li.remove(i)
                li.append(i - 1)
                li.append(i - 2)
            else:
                continue
    counter = Counter(li)
    print(counter[0], counter[1])
