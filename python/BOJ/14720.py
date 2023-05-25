N = int(input())

li = list(map(int, input().split()))

a = 0
cnt = 0

for i in li:
    if i == a != 2:
        a += 1
        cnt += 1
    elif i == 2 == a:
        a = 0
        cnt += 1
    else:
        continue

print(cnt)
