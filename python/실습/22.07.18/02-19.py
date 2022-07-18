number = int(input())
c = 0

#10씩나누어서 0이 되기 직전까지 반복문을 실행한다.
while number > 0:
    number //= 10
    c += 1
print(c)

