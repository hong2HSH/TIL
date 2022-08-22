cnt = 1

def d(n):
    n = n + sum(map(int,str(n)))
    return n
li = []

for i in range(1,10001):
    li.append(d(i))

for j in range(1,10001):
    if j not in li:
        print(j)