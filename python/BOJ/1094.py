list = [64, 32, 16, 8, 4, 2, 1]
x = int(input())
cnt = 0

for i in list:
    if i <= x:
        cnt += 1
        x -= i
        continue
print(cnt)
