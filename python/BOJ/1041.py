n = int(input())
num = list(map(int,input().split()))

if n == 1:
    print(sum(num)-max(num))

a = min(num[0],num[5])
b = min(num[1],num[4])
c = min(num[2],num[3])
num = [a,b,c]
num.sort()
sum = 0

sum3 = 1
sum2 = 2*n -2
sum1 = n**2 - sum2 - sum3

if n != 1:
    print(num[0]*(4*sum1)+num[1]*(4*sum2)+num[2]*(4*sum3)+n*n*num[0])