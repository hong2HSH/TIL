N = int(input())
cnt = 0
n = N

while 1:
    a = n // 10
    b = n % 10
    c = (a + b) % 10
    n = (b * 10) + c
    
    cnt = cnt + 1
    if n == N:
        break

print(cnt)