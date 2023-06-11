T = int(input())

for _ in range(T):
    a, b = map(int,input().split())
    cnt = 0
    if b - a == 1:
        print(1)
        continue
    elif b - a == 2:
        print(2)
    else:
        cnt += 2
        a += 1
        b -= 1
        c = b - a