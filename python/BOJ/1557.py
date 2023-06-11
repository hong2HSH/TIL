import math

k = int(input())
n = 2
cnt = 1
if k == 1:
    print(1)
else:
    while 1 :
        n += 1
        a = n **(1/2)
        print(a)
        b = math.ceil(a)
        print(b)
        if  a ** 2 != b ** 2:
            print("다름")
            cnt += 1
        else:
            print("같음")
        if cnt == k:
            break
    print(n)