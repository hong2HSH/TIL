x = int(input())
a = 1
b = 1
cnt = 0
for _ in range(x - 1):
    if (a + b) % 2 == 0:
        if a == 1:
            b += 1
        else:
            a -= 1
            b += 1
    else:
        if b == 1:
            a += 1
        else:
            a += 1
            b -= 1
print(a, "/", b, sep="")
