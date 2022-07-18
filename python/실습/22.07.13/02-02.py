def rectangle(a, b):
    return a * b, (a + b)*2
a = input().split()
c = int(a[0])
d = int(a[1])
print(rectangle(c,d))