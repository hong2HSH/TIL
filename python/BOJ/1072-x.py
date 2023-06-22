x, y = map(int, input().split())

z = (y * 100) // x
if z == 1:
    print(-1)
else:
    cnt = 1
    while 1:
        mid = x // 100
        if z == (y * 100) // x - +1:
            break
        cnt += 1
    print(cnt)
