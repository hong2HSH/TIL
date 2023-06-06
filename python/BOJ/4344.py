C = int(input())

for _ in range(C):
    li = list(map(int, input().split()))
    a = li[0]
    li = li[1:]
    sum = 0

    for i in li:
        sum += i
    avg = sum / a
    cnt = 0
    for j in li:
        if j > avg:
            cnt += 1
    print(format((cnt / a) * 100, ".3f") + "%")
