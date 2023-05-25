start = input()
cnt = 0

while 1:
    a = input()
    if a == "문제":
        cnt += 1
    elif a == "고무오리":
        if cnt > 0:
            cnt -= 1
        else:
            cnt += 2
    else:
        break
if cnt > 0:
    print("힝구")
else:
    print("고무오리야 사랑해")
