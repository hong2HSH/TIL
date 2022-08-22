N = int(input())
a = 0

for i in range(1, N+1):
    if i <= 99:
        a += 1
    else :
        x = list(map(int,str(i)))
        if x[0] - x[1] == x[1] - x[2]:
            a += 1
print(a)