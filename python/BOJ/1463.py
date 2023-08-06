n = int(input())
cnt = 0
while 1:
    cnt += 1
    if n % 3 == 0:
        n = n / 3
    elif n % 2 == 0:
        n /= 2
    else:
        n -= 1
    if n == 1:
        break
print(cnt)
