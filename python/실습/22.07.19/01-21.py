n = int(input())
r = 0
while(n > 0):
    r1 = n % 10
    r = (r * 10) + r1
    n = n // 10
print(r)