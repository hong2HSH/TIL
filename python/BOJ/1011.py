T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    sum = 0
    cnt = 0
    m = 1
    while sum < b - a:
        cnt += 1
        sum += m
        if cnt % 2 == 0:
            m += 1
    print(cnt)
