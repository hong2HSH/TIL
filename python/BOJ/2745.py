N, B = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
B = int(B)

N = N[::-1]
sum = 0

for i, n in enumerate(N):
    sum += (B**i) * (ary.index(n))
print(sum)
