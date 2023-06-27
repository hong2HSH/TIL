n = int(input())
cnt = 0
while 1:
    if n < 1:
        break
    if n >= 3:
        cnt += 1
        n -= 3
    else:
        cnt += 1
        n -= 1
if cnt % 2 == 0:
    print("CY")
else:
    print("SK")
