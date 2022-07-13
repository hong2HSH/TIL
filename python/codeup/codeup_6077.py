a = int(input())
b = int(0)
c = 0
while b <= a:
    if b%2 == 0 :
        c = c + b
    b += 1
print(c)