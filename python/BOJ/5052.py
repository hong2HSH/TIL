t = int(input())

for _ in range(t):
    a = int(input())
    e = list(map(int, str(input())))
    for i in range(a - 1):
        cnt = 0
        b = list(map(int, str(input())))
        for j in range(3):
            if e[j] == b[j]:
                cnt += 1
        if cnt == 3:
            print("NO")
            break
    if cnt != 3:
        print("YES")
