# 아스키코드
a = input()
b = 0
for i in a:
    b = ord(i) - 64
    print(b, end = ' ')