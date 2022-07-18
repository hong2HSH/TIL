n = int(input())

# 1) while 문
a = 1
sum = 0
while a <= n:
    sum += a
    a += 1
print(sum)

# 2) for 문
sum1 = 0
for i in range(1,n+1):
    sum1 += i
print(sum1)